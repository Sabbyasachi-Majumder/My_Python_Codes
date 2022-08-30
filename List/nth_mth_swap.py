print("\tNTH AND MTH ELEMENT OF LIST SWAP :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    n=(int(input("Enter Nth position no : "))-1)
    m=(int(input("Enter Mth position no : "))-1)
    print("Elements of the Array : ",end="")
    print(A)
    A[n]+=A[m]
    A[m]=A[n]-A[m]
    A[n]-=A[m]
    print("\nSwapped elements of the Array : ",end="")
    print(A)    
print("THE END")
