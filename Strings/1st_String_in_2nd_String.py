import time
from collections import Counter
print("\t1st STRING FROM 2nd STRING ")
n=1
while True :
    s1=input("\nEnter the 1st STRING (0 to exit) : ").lower()
    if s1=='0' :
        break
    s2=input("Enter the 2nd STRING : ").lower()
    st=time.time()
    d1=Counter(s1)
    d2=Counter(s2)
    for i in d1 :
        if i not in d2 or d1[i]>d2[i] :
            flg=False
            break
    if flg :
        print(s1+" is in "+s2)
    else :
        print(s1+" is not in "+s2)
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
