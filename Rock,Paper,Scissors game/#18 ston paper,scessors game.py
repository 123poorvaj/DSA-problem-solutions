ab=input("Enter your input Rock/ Paper/Scissors >> ").lower()
Aj=input("Enter Your input >>").lower()
if (ab=="rock" and Aj=="scissors") or (ab=="paper" and Aj=="rock") or (ab=="scissors" and Aj=="paper") :
    print("Abhinav Wins")
elif ab==Aj:
    print("Tie")
else:
    print("Anjali Wins")