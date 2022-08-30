import time

def b_st(l) :
    for k in range(len(l)) :
        print(l)
        for i in range(len(l)-k-1) :
            if l[i]>l[i+1] :
                tmp=l[i]
                l[i]=l[i+1]
                l[i+1]=tmp
    return l

print("\tBUBBLE SORT LIST")
while True :
    t=int(input("\nEnter terms of List (0 to exit) : "))
    if t<2 :
        break
    l=[]
    print("Enter the Elements : ")
    for i in range(t) :
        l.append(int(input("Enter the {0}th element : ".format(i+1))))
    st=time.time()
    print("Unsortd List : ",l)
    print("Sorted List : ",b_st(l))
    en=time.time()
    print("Time : ",(en-st))
print("THE END")

