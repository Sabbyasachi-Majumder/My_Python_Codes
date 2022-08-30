print("\BREAKING A LIST IN N SIZE LISTS:")
t=1
while t>0 :
    A=[]
    t=int(input("\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th terrm : ".format(i+1))))
    print("Elements of the List : ",A)
    n=int(input("Size of smaller lists :"))
    B=[A[i:i+n] for i in range(0,len(A),n)]
    for i in range(len(B)):
        print("{0}th smaller list : ".format(i+1),B[i])
print("THE END")

