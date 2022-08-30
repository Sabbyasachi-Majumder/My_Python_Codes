print("\tROTATING STRING LEFT AND RIGHT")
flg=1
while flg!=0 :
    s=input("\nEnter the STRING : ")
    n=int(input("Enter the position no : "))
    if n>len(s) :
          print("The position no os more than the length of string .Try again")
    else :
        print("Left Rotation : "+s[n:]+s[:n])
        print("Right Rotation : "+s[len(s)-n:]+s[:len(s)-n])
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
