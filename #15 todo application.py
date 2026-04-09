#create a Todo application code
a=[]
print("\n===================== WELL COME ======================")
while(True):
    choice=int(input("1.add items\n2.show items\n3.Remove the complited Task \n4.Exite\n Enter your choice >> "))
    match choice:
        case 1:
            num_of_list=int(input("Enter how many Task do you Enter >> "))
            for i in range(num_of_list):
                item=input(f"Enter the item {i+1} : ")
                a.append(item)
            print("\n")
        case 2:
            if(len(a)==0):
                print("\nNo items in the list\n")
            else:
                print("++++++++++++++++++")
                for i in range(0,len(a)):
                    print(f'{i+1} - {a[i]}')
                print("++++++++++++++++++++")
                print("\n")
        case 3:
            if(len(a)==0):
                print("\nNo items in the list\n")
            else:
                print("\nThis are all your Taks")
                print("++++++++++++++++++")
                for i in range(0,len(a)):
                    print(f'{i+1} - {a[i]}')
                print("++++++++++++++++++++")
                
                deletedItem=input("\nEnter which one you complited : ")
                for it in range(0,len(a)):
                    if a[it]==deletedItem:
                        a.remove(a[it])
                        print(f"Task number {it+1} is removed\n")
                        break

        case 4:
            print("========================Thank You==============================")
            break
        case _:
            print("\nenter the proper choice")




