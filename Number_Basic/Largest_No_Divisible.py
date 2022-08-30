import time

def div(n,x) :
    if n%x==0 :
        return n
    else :
        return div(n-1,x)

print("\tLARGEST NO DIVISIBLE : ")
while True :
    n=int(input("\nEnter the no of Digits : "))
    if n==0 :
        break
    x=int(input("Enter the no to be divided with : "))
    st=time.time()
    print("\nLargest No : ",div((10**n)-1,x))
    en=time.time()
    print("Time : ",(en-st))
print("The End")
