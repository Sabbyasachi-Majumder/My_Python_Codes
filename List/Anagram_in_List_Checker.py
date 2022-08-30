import time

def An_Chk(x,y) :
    if len(x)==len(y) :
        for i in x :
            if x.count(i)!=y.count(i) :
                return False
        return True
    return False
    
print("\tANAGRAM COLLECTOR")
n=1
while True :
    n=int(input("\nEnter the no of TERMS(0 to exit) : "))
    if n==0 :
        break
    L=[]
    print("\nEnter the TERMS :")
    for i in range(n) :
        L.append(input("Enter the {0}th term : ".format(i+1)))
    st=time.time()
    A=[]
    for i in range(len(L)-1) :
        for k in range(i+1,len(L)) :
            if An_Chk(L[i],L[k]) :
                if L[i] not in A :  A.append(L[i])
                if L[k] not in A :  A.append(L[k])
    if A :
        print("Anagrams : ",end="")
        for i in A :
            print(i," ; ",end="")
    else :
        print("There are no anagrams in the LIST ")
    if len(L)>len(A) :
        print("\nNot Anagrams : ",end="")
        for i in L :
            if i not in A :
                print(i," ; ",end="")
    else :
        print("\nThere are all anagrams in the LIST ")
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
