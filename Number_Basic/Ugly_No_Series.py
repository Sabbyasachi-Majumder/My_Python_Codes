from itertools import combinations
import time

def ugly(x) :
    l=2
    while x>1 and l<6 :
        if x%l==0 :
            x=x//l
        else :
            l+=1
    if x>1 :
        return False
    else :
        return True
    
print("\tUGLY NUMBER SERIES : ")
while True :
    n=int(input("\nEnter the no of  TERMS : "))
    if n==0 :
        break
    st=time.time()
    print("Ugly no series for ",n," terms : 1 ; ",end="")
    i=1
    c=2
    while i<n :
        if ugly(c) :
            print(c," ; ",end="")
            i+=1
        c+=1       
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


