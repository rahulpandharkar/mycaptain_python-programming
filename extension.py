a = input("Enter the name of the entire file: ")
if a.endswith('.py'):
    print("Extension is Python")
elif a.endswith('.c'): 
    print("Extension is C")
elif a.endswith('.cpp'): 
    print("Extension is C++")
else: 
    print("Extension is not determined")

