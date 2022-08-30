#An array is monotonic if it is either monotone increasing or monotone decreasing.
#An array A is monotone increasing if for all i <= j, A[i] <= A[j].
#An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

print("\tMONOTONIC SERIES CHECK :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    print(t," Elements of the Array : ",A[0],end="")
    for i in range(1,t):
        print(" , ",A[i],end="")
    if all(A[i] <= A[i + 1] for i in range(len(A) - 1)) : 
        print(" : MONOTONIC increasing series ")
    elif all(A[i] >= A[i + 1] for i in range(len(A) - 1)) :
        print(" : MONOTONIC decreasing series ")
    else :
        print(" : not MONOTONIC series ")    
print("THE END")

