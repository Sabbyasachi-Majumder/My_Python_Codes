print("\tROTATING AN ARRAY :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    d=int(input("Enter the no of terms rotating"))
    print(t," Elements of the Array : ",A[0],end="")
    for i in range(1,t):
        print(" , ",A[i],end="")
    for i in range(d) :
        for k in range(t-1) :
            c=A[k]
            A[k]=A[k+1]
            A[k+1]=c
    print("\nNew Array after {0} rotations  : ".format(d),end="")
    for i in range(t):
        print(" , ",A[i],end="")    
print("THE END")
