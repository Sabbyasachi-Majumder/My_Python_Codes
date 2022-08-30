import time

print("\tSUM OF ODD FACTORS OF A NUMBER : ")
while True :
    n=int(input("\nEnter the no (0 to exit) : "))
    st=time.time()
    if n==0 :
        break
    f=[]
    s=0
    print("Factors : ",end="")
    for i in range(1,n-1) :
        if n%i==0 :
            print(i,' ; ',end="")
            f.append(i)
    print("\nOdd Factors : ",end="")
    for i in f :
        if i%2!=0 :
            print(i,' ; ',end="")
            s+=i
    print("\nSum of Odd Factors : ",s)
    en=time.time()
    print("\nTime : ",(en-st))
print("The End")


