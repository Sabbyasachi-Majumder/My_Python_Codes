print("\tCHARACTER POSITION DELETE IN STRING")
flg=1
while flg!=0 :
    s=input("\nEnter the STRING : ")
    pos=(int(input("Enter the position no :"))-1)
    if pos>=len(s):
        print("Position no out of string length .Try again .")
    else :
        print("Given String : "+s)
        ns=''.join([s[i] for i in range(len(s)) if i!=pos])
        print("New String :"+ns)
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
