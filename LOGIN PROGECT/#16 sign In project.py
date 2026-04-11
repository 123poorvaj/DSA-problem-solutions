
userDetails={"kishore":"ki@123","poorvaj":"poorvaj@134","Adi":"Adi@321"}

count=0

for i in range (3):
    a=input("Enter your name >> ")
    b=input("Enter the password >> ")
    if (a,b) in userDetails.items():
        print("******Login Successfull****")
        break
    else:
        if count<2:
            if a not in userDetails.keys():
                print(" please check  you user name is Incorrect")
            elif userDetails[a]!=b: 
                print("please  check  your passwasdford is Incorrect")
            count+=1
            print(f"you have only {3-(count)} chance if you not enter the carrect input Account is blocked")
        else:
            print("your chance(s) complited so")
else:         
    print("Account is blocked!")

   
          


   
