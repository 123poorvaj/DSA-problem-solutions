a=input("Enter your name >> ")
b=input("Enter the password >> ")
userDetails={"kishore":"ki@123","poorvaj":"poorvaj@134","Adi":"Adi@321"}

LOGIN=False
userName=False
password=False



if (a,b) in userDetails.items():
    LOGIN=True
else :
    if a not in userDetails.keys():
        userName=True
    elif userDetails[a]!=b: 
        password=True
        
            

if LOGIN:
    print("******Login Successfull****")

if userName:
    print(" please check  you user name is Incorrect")
if password:
    print("please  check  your password is Incorrect")
