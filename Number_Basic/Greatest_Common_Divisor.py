import time

print("\tGREATEST COMMON DIVISOR : ")
while True :
    a=int(input("\nEnter the 1st no : "))
    if a==0 :
        break
    b=int(input("Enter the 2nd no : "))
    st=time.time()
    s=a if a<b else b
    while s>1 :
        if a%s==0 and b%s==0 :
            break
        else :
            s-=1
    print(s,"is common divisor of  ",a," and ",b)
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


