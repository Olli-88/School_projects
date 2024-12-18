def fibonacci_value(n):
    x = 0
    y = 1

    if n == 0 or n == 1:
        sum = n
        print(sum)
    else:    
        for i in range(1, n):
            sum = x + y
            x = y
            y = sum
        print(sum)

fibonacci_value(0)
fibonacci_value(1)
fibonacci_value(2)
fibonacci_value(8)