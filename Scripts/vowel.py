y=input("Enter a string:")
k=len(y)
u=0
l=0
v=0
c=0
for i in range(k):
    if y[i] in ['A','E','I','O','U']:
       v+=1
       u+=1
    elif y[i] in ['a','e','i','o','u']:
        v+=1
        l+=1
    else:
        if y[i].isupper()==True:
            c+=1
            u+=1
        else:
            c+=1
            l+=1
print("Number of vowels are:",v)
print("Number of consonants are:",c)
print("Number of upper case are:",u)
print("Number of lower case are:",l)  
