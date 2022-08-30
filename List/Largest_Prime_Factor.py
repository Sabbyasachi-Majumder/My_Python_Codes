import time
def prime(n) :
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True

print("\tLARGEST PRIME FACTOR OF A NUMBER : ")
while True :
    n=int(input("\nEnter the no (0 to exit) : "))
    st=time.time()
    if n==0 :
        break
    f=[]
    pf=[]
    print("Factors : ",end="")
    for i in range(2,n+1):
        if n%i==0 :
            print(i,' ; ',end="")
            f.append(i)
    if f is None :
        print("None\nThus cant have further operations")
        continue
    print("\nPrime Factors : ",end="")
    for i in f :
        if prime(i) :
            print(i,' ; ',end="")
            pf.append(i)
    if pf is None :
        print("None\nThus cant have further operations")
        continue
    print("\nLargest Prime Factor : ",max(pf))    
    en=time.time()
    print("Time : ",(en-st))
print("The End")


