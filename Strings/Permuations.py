from itertools import permutations 
print("\tPERMUTATIONS AND COMBINATIONS IN STRING")
flg=1
while flg!=0 :
    s=input("\nEnter the STRING : ")
    p=permutations(s)
    d=[]
    print("Permuattions of {0} : ".format(s))
    for i in list(p) :
        if i not in d :
            d.append(i)
            print(''.join(i))
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
