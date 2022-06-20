list = []

n = int(input("Enter the elements of the list: "))
for i in range(0,n): 
    a = int(input())
    list.append(a)
print("Positive numbers in the given list ",list,"are: ")
for i in list:
    if i>0: 
        print(i)
          


