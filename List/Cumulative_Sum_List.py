print("\PRINTING CUMULATIVE SUM OF ALL ELEMENTS IN LIST :")
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
    A=[sum(A[0:i:1]) for i in range(len(A)+1)]
    print("Cumulative sum List : ",A[1:])
print("THE END")

