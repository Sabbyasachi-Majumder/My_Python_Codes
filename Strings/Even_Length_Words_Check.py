print("\tPRINTING EVEN LENGTH WORDS IN STRING")
flg=1
while flg!=0 :
    s=input("\nEnter the larger STRING : ")
    ew=s.split(' ')
    ew=[i for i in ew if len(i)%2==0]
    if ew :
        print("Even words are : ",ew)
    else :
        print("There are no even length words") 
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
