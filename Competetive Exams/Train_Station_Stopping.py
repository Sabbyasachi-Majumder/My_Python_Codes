import time
from itertools import combinations

def check(l) :
    for i in range(len(l)-1) :
        if l[i+1]-l[i]<2 :
            return False
    return True

print("\tSTATION STOPPING NO ADJACENT STOPS : ")
while True :
    n=int(input("\nEnter the total no of Stations : "))
    if n==0 :
        break
    x=int(input("Enter the no Stops needed to make : "))
    st=time.time()
    ll=[i for i in range(n)]
    print("Combinations possible : ")
    c=1
    for i in combinations(ll,x) :
        if check(i) :
            print(c,". ",i)
            c+=1
    print("Total no of combinations posssible : ",c-1)
    en=time.time()
    print("Time : ",(en-st))
print("The End")
