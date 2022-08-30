import time

def lin_srch(l,x,p) :
    if p<len(l) :
        if  x==l[p] :   return p
        else :  return lin_srch(l,x,p+1)
    else :  return -1

print("\tLINEAR SEARCHING LIST USING RECURSION:")
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
    print("List : ",l)
    if lin_srch(l,x,0)>-1 :
        print("The no ",x," is found at {0}th position of the list . ".format(lin_srch(l,x,0)+1))
    else  :
        print("The no ",x," is not found in the list . ")
    en=time.time()
    print("Time : ",(en-st))
print("THE END")

