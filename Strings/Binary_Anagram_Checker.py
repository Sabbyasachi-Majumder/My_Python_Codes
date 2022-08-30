import time
print("\tBINARY ANAGRAM CHECKER")
n=1
while True :
    b1=int(input("\nEnter the 1st No (0 to exit) : "))
    if b1==0 :
        break
    b2=int(input("Enter the 2nd no : "))
    st=time.time()
    if bin(b1).count("1")==bin(b2).count("1") :
        print(b1,"=",bin(b1)[2:]," and ",b2,"=",bin(b2)[2:]," are Anagrams . ")
    else :
        print(b1,"=",bin(b1)[2:]," and ",b2,"=",bin(b2)[2:]," are not Anagrams . ")
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
