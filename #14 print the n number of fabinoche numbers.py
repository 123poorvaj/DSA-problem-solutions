#write a program fibinoche sirese number'''
n=int(input("Enter how many numbers in the list >> "))
a=[0,1]
for i in range (2,n):
    sum=a[i-1]+ a[i-2]
    a.append(sum)

print(a)