stack=[]

def push_items():
    element=input()
    stack.append(element)
    print(f"{element} is added")

def pop_element():
    if  not stack:
           print("stack is empty pop is not possible")
    else:
        item=stack.pop()
        print(item)

def peek_element():
    print(f"Peek element is {stack[-1]}")


def find_empty():
    if  not stack:
       print("stack is empty")
    else:
       print("stack is not empty")

def display():
    if  len(stack)==0:
           print("stack is empty")
    else:
        for i in range(len(stack)-1,0,-1):
            print(stack[i],end=' ')





print("================stack=================")
while(1):
    print("\n\n")
    print("1.push elemets\n2. pop top element\n3.peek element\n4.isempty\n5. display")
    ch=int(input("Enter your option in numbers>> "))
    match(ch):
        case 1:
            push_items()
        case 2:
            pop_element()
        case 3:
            peek_element()
        case 4:
            find_empty()
        case 5:
            display()
        case _:
            print("Enter valid input try again")


    



