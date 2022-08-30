import time

print("\tMIRROR CHARACTERS IN STRINGS ")
n=1
while True :
    s=input("\nEnter the STRING (0 to exit) : ").lower()
    if s=='0' :
        break
    n=int(input("Enter the Position No :"))
    st=time.time()
    ss=''
    for i in s[n:] :
        ii=ord(i)-97
        if ii<=13 :
            ss+=chr(122-ii)
        else :
            ss+=chr(96+(26-ii))
    print("Mirror of ",s," : ",s[:n]+ss)      
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
