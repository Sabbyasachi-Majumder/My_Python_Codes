from itertools import combinations
import time
print("\tCOMINATIONS FROM A GIVEN ARRAY : ")
while True :
    v=[]
    s=input("\nEnter the no terms (0 to exit) : ")
    if s=='0' :
        break
    for i in s :
        v.append(i)
    print("\n")
    st=time.time()
    l=[]
    for i in range(1,len(s)+1) :
        for k in range(len(s)-i) :
            l.append(s[k:i+k])
    print(l)
    en=time.time()
    print("Time : ",(en-st))
print("The End")


