print("\tCOMPUND INTEREST : ")
P=1
while P!=0 :
    P=float(input("\nEnter the PRINCIPLE (0 for exit ) : "))
    if P==0 :
        break
    T=int(input("Enter the TOTAL TIME PERIOD (YEARS) : "))
    TP=int(input("Enter the TIME PERIOD PER INTEREST : "))
    T=T*12/TP
    R=float(input("Enter the RATE (DECIMALS ) : "))
    A=P*pow((1+R/100),T)
    print("AMOUNT : {0}".format(A))
    print("COMPOUND INTEREST : {0}".format(A-P))
print("The End")
