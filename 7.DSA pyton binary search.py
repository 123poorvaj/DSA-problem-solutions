#binary search using queues
# * it is only applicabel sorted array element
# step-1 : it is find the middel element
# step -2 : it is follow  the condition
# condition-1 : if middel element is equal to element.
#               index of that element store the position than print
#condition -2 : if element is grater than the middel element.
#               it  continue to search the rigth half
# condition -3 :if element is lesser  than the middel element.
#                it  continue to search the left half  #


s=[20,45,25,46,28,46,37,91,34,257]
s.sort()
print(s)  # [20, 25, 28, 34, 37, 45, 46, 46, 91, 257]
element=int(input("Enter the element which you want to search>> "))
positon=-1 #starting take position is -1 becouse index star form 0
low=0
high=len(s)
while (low<=high):
    mid=(low +high )//2

    if  (s[mid]==element):
        position=mid
        break
    elif (s[mid]>element):
        high=mid-1

    elif (s[mid]<element):
        low = mid+1

if (positon==-1):
    print(f"Element  {element} is not prasent")
else:
   print(f" {element} is prasent at the position {positon}")
