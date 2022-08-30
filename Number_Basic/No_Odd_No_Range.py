import time

print("\tODD NOS CHECKER IN A RANGE : ")
while True :
    n=int(input("\nEnter the 1st no : "))
    if n==0 :
        break
    while True :
        m=int(input("Enter the 2nd no : "))
        if m<=n :
            print("Either the value is smaller or equal to the earlier given value . Try again ")
            continue
        break
    st=time.time()
    print("No of odd nos between ",n," and ",m," : ",(int(m**0.5)-int((n-1)**0.5)))
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


