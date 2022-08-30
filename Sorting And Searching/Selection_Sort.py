import time

def s_st(l) :
    mp=0
    for i in range(len(l)) :
        mp=i
        for k in range(i,len(l)) :
            if l[mp]>l[k] :
                mp=k
        tmp=l[mp]
        l[mp]=l[i]
        l[i]=tmp
    return l

print("\tSELECTION SORT LIST")
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
    print("Sorted List : ",s_st(l))
    en=time.time()
    print("Time : ",(en-st))
print("THE END")

