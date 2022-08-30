import time
import math
def prime(n) :
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True

print("\tPRIME REPEATING FACTOR OF A NUMBER : ")
while True :
    n=int(input("\nEnter the no (0 to exit) : "))
    cpy=n
    st=time.time()
    if n==0 :
        break
    f=[]
    pf=[]
    D=[]
    print("Factors : ",end="")
    i=2
    while cpy>1 :
        if cpy%i==0 :
            print(i,' ; ',end="")
            f.append(i)
            cpy=cpy//i
        else :
            i+=1
    print("\nPrime Factors : ",end="")
    for i in f :
        if prime(i) :
            print(i,' ; ',end="")
            pf.append(i)
    prod=1
    for i in pf:
        if i not in D :
            D.append(i)
    print("\nProduct of all unique nos : ",math.prod(D))
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


