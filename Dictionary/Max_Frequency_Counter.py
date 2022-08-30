from collections import Counter
import time
print("\tMAXIMUM FREQUENT NAME CALCUALTOR")
n=1
while True :
    n=int(input("\nEnter the no of TERMS(0 to exit) : "))
    if n==0 :
        break
    L=[]
    print("\nEnter the NAMES :")
    for i in range(n) :
        L.append(input("Enter the {0}th term : ".format(i+1)))
    st=time.time()
    D=Counter(L)
    mv=max(D.values())
    print("Result : ",end="")
    for i in D.keys() :
        if D[i]==mv :
            print(i+" ; ",end="")
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
