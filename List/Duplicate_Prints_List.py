print("\PRINTING DUPLICATES ELEMENTS IN LIST :")
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
    B=[]
    for i in range(t-1) :
        for k in range(i+1,t):
            if A[i]==A[k] and A[i] not in B:
                B.append(A[i])
    if B:
        print("New List : ",B)
    else :
        print("No duplicates found")
print("THE END")

