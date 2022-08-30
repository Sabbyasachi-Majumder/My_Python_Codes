def inp(n) :
    d={}
    for i in range(n) :
        key=input("Enter the {0}th key : ".format(i+1))
        d[key]=input("Enter the {0}th value : ".format(i+1))
    return d
    
print("\tMERGING TWO DICTIONARIES")
n=1
while True :
    n1=int(input("\nEnter the no of terms for 1st Dictionary (0 to exit) : "))
    if n1==0 :
        break
    d1=inp(n1)
    n2=int(input("\nEnter the no of terms for 2nd Dictionary : "))
    d2=inp(n2)
    print("1st Dictionary : ",d1)
    print("2nd Dictionary : ",d2)
    d1={**d1,**d2}
    print("Merged Dictionary : ",d1)
print("The End")
