print("\tODD NUMBERS IN LIST :",end=" ")
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
    print("Even nos : ",[i for i in A if i%2!=0])
print("THE END")
