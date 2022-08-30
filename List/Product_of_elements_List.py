import math
print("\tPRODUCT OF ELEMENTS IN LIST :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th terrm : ".format(i+1))))
    print("Elements of the List : ",A)
    print("Product :",math.prod(A))
print("THE END")

