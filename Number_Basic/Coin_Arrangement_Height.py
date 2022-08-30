import time

print("\tCOIN ARRANGEMENT HEIGHT : ")
while True :
    n=int(input("\nEnter the no of COINS : "))
    if n==0 :
        break
    st=time.time()
    print("Triangle  : ")
    i=1
    while n>0 :
        print("* "*i)
        i+=1
        n-=i
    print("\nNo of Lines formed : ",i-1)
    en=time.time()
    print("Time : ",(en-st))
print("The End")


