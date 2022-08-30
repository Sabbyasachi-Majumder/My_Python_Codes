#Input : arr[] = {12, 10, 5, 6, 52, 36}
#            k = 2
#Output : arr[] = {5, 6, 52, 36, 12, 10}

#Explanation : Split from index 2 and first 
#part {12, 10} add to the end .

#Input : arr[] = {3, 1, 2}
#           k = 1
#Output : arr[] = {1, 2, 3}
#Explanation : Split from index 1 and first
#part add to the end.

print("\tRVERSE ADD PARTS OF AN ARRAY :",end=" ")
t=1
while t>0 :
    A=[]
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print("Enter the elements :")
    for i in range(t):
        A.append(int(input("Enter {0}th no : ".format(i+1))))
    d=int(input("Enter the no of terms to be transfered :"))
    print(t," Elements of the Array : ",A[0],end="")
    for i in range(1,t):
        print(" , ",A[i],end="")
    for i in range(d) :
        for k in range(t) :
            if k+1>t-1 :
                break
            c=A[k]
            A[k]=A[k+1]
            A[k+1]=c
    print("\nNew Array after {0} places transfered to the end  : ".format(d),end="")
    for i in range(t):
        print(" , ",A[i],end="")    
print("THE END")

