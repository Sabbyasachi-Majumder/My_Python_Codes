print("\tSUM OF DICTIONARY VALUES")
n=1
while True :
    n=int(input("\nEnter the no of terms (0 to exit) : "))
    if n==0 :
        break
    d={}
    for i in range(n) :
        key=input("Enter the {0}th key : ".format(i+1))
        d[key]=int(input("Enter the {0}th value : ".format(i+1)))
    print("Dictionary : ",d)
    s=0
    for i in d.values() :
        s+=i
    print("Sum of Values : ",s)
print("The End")
