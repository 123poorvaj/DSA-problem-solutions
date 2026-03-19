#read the 3 number and find the larger number using python program
a=int(input())
b=int(input())
c=int(input())

if a>=b and a>=c:
    larger=a
elif b>=a and b>=c:
    larger=b
else:
    larger=c 

print(f"{larger} is the largest number")