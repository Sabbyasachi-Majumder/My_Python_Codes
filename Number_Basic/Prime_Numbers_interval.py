def prime_check(x):
    for i in range (2,x):
        if x%i==0 :
            return False
    return True

print("\tPRIME NUMBERS IN AN INTERVAL",end=" ")
n=1
while n>0 :
    n=int(input("\n\nEnter the smaller no (-1 to exit):"))
    if n<0 :
        break
    m=int(input("Enter the larger no : "))
    print("PRIME numbers between {0} and {1} : ".format(n,m),end="")
    for i in range(n,m+1):
        if prime_check(i):
            print(i,end=" ;")
print("THE END")
