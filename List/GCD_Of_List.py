import time

def Gcd(a,b) :
    for i in range(min(a,b),0,-1) :
        if a%i==b%i==0 :
            return i

print("\tGREATEST COMMON DIVISOR OF AN LIST : ")
while True :
    n=int(input("\nEnter the no of terms (0 to exit) : "))
    l=[]
    if n==0 :
        break
    print("Enter the elements : ")
    for i in range(n) :
        l.append(int(input("Enter the {0}th element : ".format(i+1))))
    st=time.time()
    gcd=0
    ggcd=0
    print("GCDs : ")
    for i in range(n-1) :
        gcd=Gcd(l[i],l[i+1])
        print(i+1,". (",l[i]," ; ",l[i+1],") : ",gcd)
        ggcd=Gcd(gcd,l[i])
    print("\nTotal GCD :",ggcd)
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


