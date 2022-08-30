print("\tHANDLING A MISING KEY IN DICTIONARY")
n=1
while True :
    n=int(input("\nEnter the no of terms (0 to exit) : "))
    if n==0 :
        break
    d={}
    for i in range(n) :
        key=input("Enter the {0}th key : ".format(i+1))
        d[key]=input("Enter the {0}th value : ".format(i+1))
    x=input("Enter the required key : ")
    print("Dictionary : ",d)
    if d.get(x) :    
        print("Value at "+x+" key : ",d[x])
    else :
        print("There is no "+x+" key .")
print("The End")
