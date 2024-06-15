import ollama
import os
from tqdm import tqdm
import argparse
import json

def load_categories(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def generate_hint(categories):
    hint = "The Python code is buggy and it's likely to be within one of these categories:\n"
    for error in categories['runtime_errors']:
        hint += f"- {error['type']}: {error['description']}\n"
    hint += "\nCan you identify the error and fix it? Give me a fixed version of the code."
    return hint

def response_codeonly(content):
    content = "This code is buggy. Can you help me fix the code?\n\n" + content
    response = ollama.chat(
        model="Llama3",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    return response["message"]["content"]

def response_with_description(content, description):
    content = "This code is an attempt to solve the following problem:\n" + description + "\n\nHowever, the code is buggy. Can you help me fix the code?\n\n" + content
    # print(content)
    response = ollama.chat(
        model="Llama3",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    return response["message"]["content"]

def response_with_hint(content, hint):
    content = hint + "\n\n" + content
    # print(content)
    response = ollama.chat(
        model="Llama3",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    return response["message"]["content"]

def read_buggy_files(base_dir):
    all_data = {}
    
    # List all entries in the base_directory
    entries = os.listdir(base_dir)
    
    for entry in entries:
        entry_path = os.path.join(base_dir, entry)
        
        if os.path.isdir(entry_path):
            # Look for Python files and description.txt in the subdirectory
            files = os.listdir(entry_path)
            if(len(files) == 0):
                continue
            all_data[entry] = {"code": {}, "description": ""}
            description_file = os.path.join(entry_path, "description.txt")
            
            if os.path.exists(description_file):
                with open(description_file, 'r') as df:
                    description = df.read()
            else:
                description = ""
            all_data[entry]["description"] = description

            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(entry_path, file)
                    with open(file_path, 'r') as f:
                        content = f.read()
                    
                    
                    all_data[entry]["code"][file] = content
    
    return all_data

def create_fixed_directory_structure(base_directory, target_directory):
    for root, dirs, files in os.walk(base_directory):
        # Create corresponding directory structure in target_directory
        relative_path = os.path.relpath(root, base_directory)
        target_path = os.path.join(target_directory, relative_path)
        if not os.path.exists(target_path):
            os.makedirs(target_path)

def write_fixed_files(args):
    buggy_files = read_buggy_files(args.buggy_dir)

    categories = load_categories(args.categories_file)
    hint = generate_hint(categories)
    create_fixed_directory_structure(args.buggy_dir, args.result_dir)
    
    for question, data in tqdm(buggy_files.items(), desc="Processing files", unit="question"):
        description = data["description"]
        code_files = data["code"]
        
        for file_name, content in code_files.items():
            if args.mode == 'codeonly':
                fixed_content = response_codeonly(content)
            elif args.mode == 'description':
                fixed_content = response_with_description(content, description)
            else:
                fixed_content = response_with_hint(content, hint)
            # Get the relative path of the file to maintain the same structure
            relative_path = os.path.join(question, file_name)
            target_file_path = os.path.join(args.result_dir, os.path.splitext(relative_path)[0] + '.txt')
            
            with open(target_file_path, 'w') as f:
                f.write(fixed_content)
            print(f"Processed: {relative_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix buggy Python files.')
    parser.add_argument('--buggy_dir', type=str, help='Path to the directory containing buggy files', default='Buggy')
    # parser.add_argument('--result_dir', type=str, help='Path to the directory where fixed files will be saved', default='Categories-Response')
    parser.add_argument('--mode', type=str, help='Mode of operation (codeonly or description)', default='hint', choices=['codeonly', 'description', 'hint'])
    parser.add_argument('--categories_file', type=str, help='Path to the categories JSON file', default='categories.json')
    args = parser.parse_args()
    if args.mode == 'codeonly':
        args.result_dir = 'CodeOnly-Response'
    elif args.mode == 'description':
        args.result_dir = 'Description-Response'
    else:
        args.result_dir = 'Categories-Response'

    # Fix the buggy files and write them to the target directory
    write_fixed_files(args)