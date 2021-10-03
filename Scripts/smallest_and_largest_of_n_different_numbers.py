#python program to display smallest and largest of n different numbers
n=int(input("Enter a limit"))
m=int(input("Enter first number"))
min=m
max=m
print("Enter next",n-1,"numbers")
for i in range(2,n+1):
     m=int(input())
     if m>max:
        max=m
     elif m<min:
          min=m
print("\nlargest number is",max)
print("\nsmallest number is",min)