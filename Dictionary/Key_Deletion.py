print("\tDELETION OF DICTIONARY KEY")
n=1
while True :
    n=int(input("\nEnter the no of terms (0 to exit) : "))
    if n==0 :
        break
    d={}
    for i in range(n) :
        key=input("Enter the {0}th key : ".format(i+1))
        d[key]=input("Enter the {0}th value : ".format(i+1))
    print("Dictionary : ",d)
    x=input("Enter the key to be deleted : ")
    if d.get(x) :
        print("Deleted value of key {0} :".format(x),d.pop(x))
        print("After deletion dictionary : ",d)
    else :
        print("Key "+x+" not found ")
print("The End")
