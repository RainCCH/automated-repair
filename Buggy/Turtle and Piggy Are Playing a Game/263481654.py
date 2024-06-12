def max_score(t, test_cases):
    results = []
    
    for case in test_cases:
        l, r = case
        
        # We start by trying x = r and count the steps to reduce x to 1
        max_x = r
        score = 0
        
        while max_x > 1:
            for p in range(2, max_x + 1):
                if max_x % p == 0:
                    max_x //= p
                    score += 1
                    break
        
        results.append(score)
    
    return results

results = max_score(t, test_cases)
for result in results:
    print(result)