from collections import Counter
import time
print("\tFINDING KTH NON REPEATING CHARACTER")
n=1
while True :
    s=input("\nEnter the STRING (END to exit) : ")
    if s.upper()=='END' :
        break
    n=int(input("Enter the K : "))
    st=time.time()
    d=Counter(list(s))
    if len(d)<n :
        print("The lengtth of String is more than k .Try again ")
    else :
        print("Result : ",end="")
        for i in d :
            if d[i]==1 :
                if n==1 :
                    print(i)
                    break
                else : n-=1
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
