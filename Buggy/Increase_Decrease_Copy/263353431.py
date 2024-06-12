def solve():
  """Solves the problem for a given test case."""
  num_test_cases = int(input())  # Read number of test cases

  for _ in range(num_test_cases):
    array_size = int(input())  # Read size of the array

    # Read elements into arrays A and B
    array_a = []
    for _ in range(array_size):
      array_a.append(int(input()))

    array_b = []
    for _ in range(array_size + 1):
      array_b.append(int(input()))

    possible = True  # Flag to check if operation is possible
    operation_count = 0

    # Calculate initial operation count for absolute differences
    for i in range(array_size):
      operation_count += abs(array_a[i] - array_b[i])

    last_element_b = array_b[array_size - 1]  # Store last element of B

    # Check if conditions are met for any element in A
    for i in range(array_size):
      if array_a[i] >= array_b[i]:
        if last_element_b >= array_b[i] and last_element_b <= array_a[i]:
          possible = False
          break
      else:
        if last_element_b <= array_b[i] and last_element_b >= array_a[i]:
          possible = False
          break

    # Additional operation needed if conditions not met
    if not possible:
      operation_count += 1

    else:
      # Find minimum distance required for additional operation
      min_distance = float('inf')
      for i in range(array_size):
        min_distance = min(min_distance, abs(array_b[i] - last_element_b))
        min_distance = min(min_distance, abs(array_a[i] - last_element_b))

      operation_count += min_distance + 1  # Add distance and final operation

    print(operation_count)  # Print the operation count

if __name__ == "__main__":
  solve()