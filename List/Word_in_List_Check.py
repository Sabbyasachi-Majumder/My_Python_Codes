print("\tGIVEN WORD EXISTENCE IN LIST :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(input("Enter {0}th terrm : ".format(i+1)))
    w=input("Enter word : ")
    print("Elements of the List : ",end="")
    print(A)
    if w in A :
       print("Word found")
    else :
        print("Word not found")    
print("THE END")
