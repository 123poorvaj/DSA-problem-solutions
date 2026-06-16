''' 
    *
  * * *
 * * * *
  * * *
    *
 '''

 #write a code to print a diamond 
n=int(input())
for i in range(1,n+1):
    space=n-i 
    stars=2*i-1
    row =space*("  ")+"* "*stars
    print(row)
j=n-1
while j>=1:
    space=n-j 
    stars=(2*j)-1
    row =space*("  ")+"* "*stars 
    print(row)
    j-=1
