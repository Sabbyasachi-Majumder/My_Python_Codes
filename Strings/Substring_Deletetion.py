def delt(ls,ss) :
    for i in range(len(ls)-len(ss)) :
            if ss==ls[i:i+len(ss)] :
                return (ls[:i]+ls[i+len(ss):])
            
print("\tSUBSTRING DELETION FROM STRING")
flg=1
while flg!=0 :
    ls=input("\nEnter the LARGER STRING : ")
    ss=input("Enter the SMALLER STRING : ")
    if len(ss)>len(ls) :
        print("The length of smaller string is more than the larger string .Try again")
    else :
        while ls.find(ss) :
            ls=delt(ls,ss)
        print(ls)
        if ls :
            print("The larger string fully deleteable by smaller string .")
        else :
            print("The larger string is not fully deleteable by smaller string .")          
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
