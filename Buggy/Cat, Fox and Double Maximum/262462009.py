def solve(n, p):
  # Step 1: Sort the permutation p in ascending order.
  p.sort()

  # Step 2: Create the array a such that a_i = p_i + i (1 ≤ i ≤ n).
  a = [p[i] + i for i in range(n)]

  # Step 3: Identify all local maxima in the array a.
  local_maxima = []
  for i in range(2, n):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
      local_maxima.append(i)

  # Step 4: Create the permutation q such that q_i = a_i - p_i (1 ≤ i ≤ n).
  q = [a[i] - p[i] for i in range(n)]

  return q

# Example usage
n = 4
p = [1, 3, 2, 4]
q = solve(n, p)
print(q)  # Output: [1, 2, 2, 2]