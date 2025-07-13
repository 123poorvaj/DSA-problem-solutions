l=[23,45,67,123,34]
x=int(input("Enter the number to be searched>> "))
position=-1
for i in range(0,len(l)):
    if l[i]==x:
        position=i
        break
if position==i:
    print(f"{x} is present at index {position}")
else:
    print(f"{x} is not  present in the list")

