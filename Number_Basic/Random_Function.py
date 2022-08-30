import random
print("\tRANDOM FUNCTION TO GENERATE A NO \n\n")

while True :
    print("Random No : ",random.randrange(1,11,1))
    ch=int(input("Do you wanna continue  ? (1 for Yes || 0 for No) : "))
    if ch is 0 :
        break
print("The End .")
    
