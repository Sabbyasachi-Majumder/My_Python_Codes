def prime_check(x):
    for i in range (2,x):
        if x%i==0 :
            return False
    return True

print("\tPRIME NUMBERS IN AN INTERVAL",end=" ")
n=1
while n>0 :
    n=int(input("\n\nEnter the NUMBER (-1 to exit):"))
    if n<0 :
        break
    if prime_check(n):
        print(n," is a prime number")
    else :
        print(n," is not a prime number")
print("THE END")
