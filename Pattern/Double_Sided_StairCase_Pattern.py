print("\tDOUBLE SIDED STAIRCASE STAR PATTERN ")
while True :
    while True :
        n=int(input("\nEnter the no of lines (0 to exit) : "))
        if n%2==0 :
            break
        else :
            print("Only even nos are accepted as N .Try again ",end="")
    if n==0 :
        break
    print("N : ",n)
    for i in range (1,n+1):
        if i%2==1 :
            print("\t"*((n-i-1)//2)+"*\t"*(i+1))
        else :
            print("\t"*((n-i)//2)+"*\t"*i)
print("The End")
