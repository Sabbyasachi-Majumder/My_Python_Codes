print("\tBINARY SEARCHING LIST USING LOOP:")
t=1
while t>0 :
    t=int(input("\nEnter terms of List (0 to exit) : "))
    if t<1 :
        break
    l=[]
    print("Enter the Elements : ")
    for i in range(t) :
        l.append(int(input("Enter the {0}th element : ".format(i+1))))
    x=int(input("\nEnter tthe number to be searched : "))
    print("Unsorted List : ",l)
    l=sorted(l)
    print("Sorted list : ",l)
    lft=0
    ryt=len(l)-1
    flg=False
    
    while lft<=ryt :
        mid=(ryt+lft)//2
        if  x>l[mid] :
            lft=mid+1
        elif x<l[mid] :
            ryt=mid-1
        else :
            flg=True
            print("The no ",x," is found at {0}th position of the list . ".format(mid+1))
            break
        
    if flg is False :
        print("The no ",x," is not found in the list . ")
print("THE END")

