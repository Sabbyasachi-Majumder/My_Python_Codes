import time

print("\tTOTAL NO OF COMMON DIVISORS : ")
while True :
    a=int(input("\nEnter the 1st no : "))
    if a==0 :
        break
    b=int(input("Enter the 2nd no : "))
    st=time.time()
    c=0
    print("common Divisors : ",end="")
    for i in range(1,min(a,b)+1) :
        if a%i==b%i==0 :
            print(i," ; ",end="")
            c+=1
    print("\nTotal no of common divisors : ",c)
    en=time.time()
    print("Time : ",(en-st))
print("The End")


