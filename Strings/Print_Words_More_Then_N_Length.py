print("\tPRINTING WORDS OF LENGTH MORE THAN N")
flg=1
while flg!=0 :
    s=input("\nEnter the larger STRING : ")
    w=s.split(' ')
    n=int(input("Enter the length : "))
    print("Words more than {0} in length : ".format(n),end="")
    for i in w :
        if len(i)>=n :
            print(i+" ",end="")
    flg=int(input("\n\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
