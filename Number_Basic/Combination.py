from itertools import combinations
import time
print("\tCOMINATIONS FROM A GIVEN ARRAY : ")
n=1
while n>0 :
    v=[]
    n=int(input("\nEnter the no terms (0 to exit) : "))
    if n==0 :
        break
    print("Numbers : ",end="")
    for i in range(n):
        print(i+1,end="")
        v.append(i+1)
    print("\n")
    st=time.time()
    l=[]
    for i in range(1,n+1):
        l.append(list(combinations(v,i)))
    for i in l :
        for j in i :
            for k in j :
                print("  ",k,"@",end="")
            print("\n")
        print("\n")    
    en=time.time()
    print("Time : ",(en-st))
print("The End")


