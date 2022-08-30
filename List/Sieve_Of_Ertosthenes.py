from itertools import combinations
import time

print("\tSIEVE OF ERTOSTHENES (PRIME NO) : ")
while True :
    n=int(input("\nEnter the limit : "))
    if n==0 :
        break
    st=time.time()
    pn=[2,3,5,7]
    l=[i for i in range(2,n+1)]
    for i in pn :
        m=2
        while i*m<=n :
            try :
                del l[l.index(i*m)]
            except ValueError :
                pass
            m+=1       
    print("Prime numbers under ",n," : ",l)
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


