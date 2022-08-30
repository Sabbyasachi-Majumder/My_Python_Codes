print("\t1ST NTH ELEMENT OF LIST SWAP :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    print("Elements of the Array : ",end="")
    print(A)
    A[0]+=A[-1]
    A[-1]=A[0]-A[-1]
    A[0]-=A[-1]
    print("\nSwapped elements of the Array : ",end="")
    print(A)    
print("THE END")

