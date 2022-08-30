print("\tSUM OF NO IN AN ARRAY :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    print(t," Elements of the Array : ",A[0],end="")
    for i in range(1,t):
        print(" , ",A[i],end="")
        A[0]+=A[i]
    print("\nSum of elements : ",A[0])
print("THE END")
