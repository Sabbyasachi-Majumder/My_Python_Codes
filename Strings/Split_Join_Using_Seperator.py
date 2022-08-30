print("\tSPLIT AND JOIN USING GIVEN SEPERATOR")
flg=1
while flg!=0 :
    s=input("\nEnter the  STRING : ")
    w=s.split(' ')
    c=input("Enter the seperator : ")
    print("Seperator is : {0}  New STRING : ".format(c),end="")
    for i in range(len(w)):
        if i !=len(w)-1 :
            print(w[i]+c,end="")
        else :
            print(w[i])
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
