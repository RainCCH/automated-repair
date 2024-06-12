def integer_to_binary(x):
    if x == 0:
        return "0"
    
    binary_digits = []
    while x > 0:
        remainder = x % 2
        binary_digits.append(str(remainder))
        x = x // 2
    
    # Reverse the list of binary digits to get the correct binary representation
    binary_digits.reverse()
    
    # Join the list to form a string
    binary_string = ''.join(binary_digits)
    
    print(len(binary_string))
    x=binary_string.split("")
    print(*x)
t=int(input())
for i in range(t):
    x=int(input())
    integer_to_binary(x)