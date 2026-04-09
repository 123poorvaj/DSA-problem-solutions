#check the number of aplhabets ,digits and special carecter prasent in the given string
a="ABCabc123+*%-#"
num_of_alpha=0
num_of_digits=0
num_of_specialCarecter=0
for i in range(0,len(a)):
    if a[i].isalpha():
        num_of_alpha +=1
    elif a[i].isdigit():
        num_of_digits +=1
    else:
        num_of_specialCarecter+=1

print("number of alphabeds : ",num_of_alpha)
print("number of digits : ",num_of_digits)
print("number of specialCarecters : ",num_of_specialCarecter)