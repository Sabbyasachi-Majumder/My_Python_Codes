print("\tSIMPLE INTEREST : ")
S=1
while S!=0 :
    S=float(input("\nEnter the SUM (0 for exit ) : "))
    if S==0 :
        break
    T=int(input("Enter the TIME PERIOD : "))
    R=float(input("Enter the RATE (DECIMALS ) : "))
    A=float(S*T*R/100)
    print("AMOUNT : {0}".format(A))
print("The End")
