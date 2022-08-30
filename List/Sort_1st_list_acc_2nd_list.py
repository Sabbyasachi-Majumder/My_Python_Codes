def inp(t):
    A=[]
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th terrm : ".format(i+1))))
    return A

print("\SORT THE 1ST LIST ACC TO 2ND LIST:")
t=1
while t>0 :
    t=int(input("Enter terms of 1st List :"))
    if t<1 :
        break
    A=inp(t)
    B=inp(int(input("Enter terms of 2nd List :")))
    if len(A)!=len(B) :
        print("The lengths of two lists are not matching . Try again .")
        continue
    else :
        print("Elements of the 1st List : ",A)
        print("Elements of the 2nd List : ",B)
        Z=zip(B,A)
        C=[x for _, x in sorted(Z)]
    print("FULL Sorted list : ",Z)
    print("Sorted list : ",C)
print("THE END")

