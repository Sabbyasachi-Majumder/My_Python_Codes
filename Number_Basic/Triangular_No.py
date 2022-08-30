import time

print("\tTRIANGULAR NUMBER CHECKER : ")
while True :
    n=int(input("\nEnter the no : "))
    cpy=n
    if n==0 :
        break
    st=time.time()
    print("Triangle formed within ",n," : ")
    i=1
    while cpy>=i :
        print("* "*i)
        cpy-=i
        i+=1
        
    if cpy==0 :
        print(n," is a Triangular no ")
    else:
        print(n," is not Triangular no ")        
    en=time.time()
    print("Time : ",(en-st))
print("The End")
