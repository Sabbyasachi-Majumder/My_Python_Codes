import time

print("\tREMOVE 1 CHAR TO MAKE ALL CHAR FREQUENCY SAME ")
n=1
while True :
    s=input("\nEnter the 1st STRING (0 to exit) : ").lower()
    if s=='0' :
        break
    st=time.time()
    d={}
    for i in s:
        if i in d :
            d[i]+=1
        else :
            d[i]=1
    flg=False
    if all(d[i]==d[s[0]] for i in d) :
        print("The STRING is already perfect ")
    else :
        for i in d :
            d[i]-=1
            print(d)
            if all(d[k]==d[s[0]] for k in d if d[k]!=0) :
                print("If we remove one "+i+" from ",s," ; we get frequency of all letters are same i.e  ",d[s[0]])
                flg=True
                break
            d[i]+=1
        if flg is False :
            print("Cant delete any one character from ",s," to make all character frequencies same .")
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
