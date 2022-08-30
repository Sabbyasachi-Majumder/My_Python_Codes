import time

print("\tBINARY PALLINDROME CHECKER : ")
while True :
    n=int(input("\nEnter the limit : "))
    if n==0 :
        break
    st=time.time()
    b=bin(n)[2:]
    if b==b[::-1] :
        print(n," ie ",b," is a pallindrome binary no .")
    else :
        print(n," ie ",b," is not a  pallindrome binary no .")
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


