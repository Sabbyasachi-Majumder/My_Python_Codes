print("\tPRINT UNCOMMON WORDS FROM 2 STRINGS")
flg=1
while flg!=0 :
    s1=input("\nEnter the 1st STRING : ")
    s2=input("Enter the 2nd STRING : ")
    ss1=s1.split(' ')
    ss2=s2.split(' ')
    ss3=[]
    for i in ss1 :
        if i not in ss2 and i not in ss3 :
            ss3.append(i)
    for i in ss2 :
        if i not in ss1 and i not in ss3 :
            ss3.append(i) 
    if ss3 :
        print("Uncommon woprds from both strings :",ss3)
    else :
        print("No uncommon words found . ")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
