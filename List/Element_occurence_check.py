print("\tNO OF TIMES AN ELEMENT OCCURS IN LIST :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(input("Enter {0}th terrm : ".format(i+1)))
    w=input("Enter the element :")
    print("Elements of the List : ",A)
    c=0
    for i in A :
        if i==w :
            c+=1
    print(w," occurs ",c," times .")
print("THE END")

