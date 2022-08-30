print("\tFACTORIAL OF NUMBER : ")
n=1
while n!=0 :
    n=int(input("\nEnter the NUMBER (0 for exit ) : "))
    if n==0 :
        break
    cpy=n
    s=1
    while cpy>1 :
        s*=cpy
        cpy-=1
    print("Factorial is : {0}".format(s))
print("The End")
