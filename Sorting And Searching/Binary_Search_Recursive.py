import time

def bin_srch(l,x,lft,ryt) :
    mid=(lft+ryt)//2
    if ryt>=lft :
        if  x>l[mid] :
            return bin_srch(l,x,mid+1,ryt)
        elif x<l[mid] :
            return bin_srch(l,x,lft,mid-1)
        else :
            return mid
    else :
        return -1

print("\tBINARY SEARCHING LIST USING RECURSION:")
t=1
while t>0 :
    t=int(input("\nEnter terms of List (0 to exit) : "))
    if t<1 :
        break
    l=[]
    print("Enter the Elements : ")
    for i in range(t) :
        l.append(int(input("Enter the {0}th element : ".format(i+1))))
    x=int(input("Enter tthe number to be searched : "))
    st=time.time()
    print("Unsorted List : ",l)
    l=sorted(l)
    print("Sorted list : ",l)
    if bin_srch(l,x,0,len(l)-1)>-1 :
        print("The no ",x," is found at {0}th position of the list . ".format(bin_srch(l,x,0,len(l)-1)+1))
    else  :
        print("The no ",x," is not found in the list . ")
    en=time.time()
    print("Time : ",(en-st))
print("THE END")

