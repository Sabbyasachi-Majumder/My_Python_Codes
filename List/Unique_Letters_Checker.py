import time

print("\tALL UNIQUE LETTERS IN STRING : ")
while True :
    s=input("\nEnter the String (0 to exit) : ")
    if s=='0' :
        break
    st=time.time()
    if all([s.count(i)==1 for i in s]) :
        print("All letters are unique in "+s)
    else :
        print("All letters are not unique in "+s)
    en=time.time()
    print("Time : ",(en-st))
print("The End")
