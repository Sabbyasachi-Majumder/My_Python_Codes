import time

print("\tTRIANGULAR MATCHSTICK NUMBER : ")
while True :
    n=int(input("\nEnter the no of floors : "))
    cpy=n
    if n==0 :
        break
    st=time.time()
    print("No of matchsticks required : ",3*sum([i for i in range(1,n+1)]))    
    en=time.time()
    print("Time : ",(en-st))
print("The End")
