def fibonacci(n):
    if n<=1:
     return n
    else: 
        return (fibonacci(n-1) + fibonacci (n-2)) 


a = int(input("Enter the limit for the fibonacci sequence: "))
if a<0: 
    print("Enter a positive number")

else: 
    print("Fibonacci Sequence till", a, "terms is: ")
    for i in range(a): print(fibonacci(i), end= " ")


