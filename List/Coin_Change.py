from itertools import combinations
import time

def change(l,x) :
    ll=[]
    n=len(l)-1
    while x>0 :
        print(x)
        if x-l[n]>0 :
            ll.append(l[n])
            x-=l[n]
        else :
            n-=1
    return ll
    
print("\tCOMINATIONS OF CHANGES FOR A COIN : ")
while True :
    c=[]
    nn=[]
    x=int(input("\nEnter the Amount (0 to exit) : "))
    if x==0 :
        break
    n=int(input("\nEnter the no of coins : "))
    print("Coins : ")
    for i in range(n):
        nn.append(int(input("Enter the {0}th coin : ".format(i+1))))
    print("\n")
    st=time.time()
    for i in range(1,n+1) :  #finding all the comnbinations from given coins
        c.append(list(combinations(nn,i)))
    cc=[]
    res=[]
    for i in c :    #To find all the eligible combinations of coins
        for k in i :
            if sum(k)<=x :
                cc.append(k)
                res.append(change(list(k),x))
    print("Combinations : ",c)
    print("Eligible Combinations : ",cc)
    print("Changes equalling ",x," : ")
    for i in range(len(res)) :
        print(i+1," . ",cc[i]," : ",res[i])
    en=time.time()
    print("Time : ",(en-st))
print("The End")


