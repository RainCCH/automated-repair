import ollama
import os
from tqdm import tqdm
import argparse

def fix_code(content):
    question = content
    response = ollama.chat(
        model="Llama3",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response["message"]["content"]

def read_buggy_files(base_dir):
    buggy_files = []
    
    # Traverse through all subdirectories under base_directory
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    buggy_files.append((file_path, content))
    
    return buggy_files

def create_fixed_directory_structure(base_directory, target_directory):
    for root, dirs, files in os.walk(base_directory):
        # Create corresponding directory structure in target_directory
        relative_path = os.path.relpath(root, base_directory)
        target_path = os.path.join(target_directory, relative_path)
        if not os.path.exists(target_path):
            os.makedirs(target_path)

def write_fixed_files(buggy_files, base_directory, target_directory):
    create_fixed_directory_structure(base_directory, target_directory)
    
    for file_path, content in tqdm(buggy_files, desc="Processing files", unit="file"):
        fixed_content = fix_code(content)
        # Get the relative path of the file to maintain the same structure
        relative_path = os.path.relpath(file_path, base_directory)
        target_file_path = os.path.join(target_directory, os.path.splitext(relative_path)[0] + '.txt')
        
        with open(target_file_path, 'w') as f:
            f.write(fixed_content)
        print(f"Processed: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix buggy Python files.')
    parser.add_argument('--buggy_dir', type=str, help='Path to the directory containing buggy files', default='Buggy')
    parser.add_argument('--result_dir', type=str, help='Path to the directory where fixed files will be saved', default='Fixed')
    args = parser.parse_args()

    base_directory = args.buggy_dir
    target_directory = args.result_dir

    # Read the buggy files
    buggy_files = read_buggy_files(base_directory)
    print(f'Number of buggy files found: {len(buggy_files)}\n')

    # Fix the buggy files and write them to the target directory
    write_fixed_files(buggy_files, base_directory, target_directory)