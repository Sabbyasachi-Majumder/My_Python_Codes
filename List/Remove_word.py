print("\tREMOVE GIVEN WORD NTH TIME RECURENCE :",end=" ")
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
    n=int(input("Enter recurence no : "))
    print("Elements of the List : ",end="")
    print(A)
    flg=False
    c=0
    for i  in range(len(A)) :
        if A[i]==w :
            c+=1
            if c==n :
                flg=True
                A.pop(i)
                break
    if flg :
       print("New List : ",A,end="")
    else :
        print("Word :",w," not present ",n," times.")    
print("THE END")
