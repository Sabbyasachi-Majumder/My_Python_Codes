import time

def check(n):
    cpy=n
    while cpy>0 :
        if cpy%10==0 or n%(cpy%10)!=0 :
            return False
        cpy=cpy//10
    return True

print("\tDIGITS DIVIDING NUMBERS : ")
while True :
    n=int(input("\nEnter the no : "))
    if n==0 :
        break
    st=time.time()
    if check(n) :
        print(n," is divisible by its digits ")
    else:
        print(n," is not divisible by its digits ")        
    en=time.time()
    print("Time : ",(en-st))
print("The End")
