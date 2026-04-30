def pattern(n):
    if n == 1:
        print("*")
        return
    
    pattern(n - 1)   # recursive call
    
    print("* " * n)  # print after returning


# Example
pattern(4)