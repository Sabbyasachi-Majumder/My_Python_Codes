import time

def in_st(l) :
    for i in range(1,len(l)) :
        key=l[i]                   
        k=i-1
        while k>-1 and l[k]>key :
            print(l)
            l[k+1]=l[k]
            k=k-1
        l[k+1]=key
    return l

print("\tINSERTION SORT LIST")
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
    print("Sorted List : ",in_st(l))
    en=time.time()
    print("Time : ",(en-st))
print("THE END")

