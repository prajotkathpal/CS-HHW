def generate_fibonacci(n):
    fibonacci_series = [0, 1] 
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]  
        fibonacci_series.append(next_term)
    return fibonacci_series


num_terms = int(input("Enter the number of terms in the Fibonacci series: "))


fibonacci_series = generate_fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:")
print(fibonacci_series)
print ("Fibonacci Sequence is a series in which each number is a sum of its two preceeding digits")
