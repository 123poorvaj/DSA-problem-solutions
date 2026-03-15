#sum of the natural numbers 
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i
    if(i<n):
        print(i, end="+") #use print horizontaliy
print(f"{i}=", sum)
