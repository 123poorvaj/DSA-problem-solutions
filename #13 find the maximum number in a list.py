#print the maximum number in a list
a=[6,11,21,1,7,46,14]
max=a[0]
for i in range(1,7):
    if(a[i]>max):
        max=a[i]
print(f"max={max}")