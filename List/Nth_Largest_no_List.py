print("\tNth LARGEST NUMBER IN LIST :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(input("Enter {0}th terrm : ".format(i+1)))
    m=int(input("Enter the amount :"))
    print("Elements of the List : ",A)
    A.sort()
    print("Largest element :",A[-m:])
print("THE END")