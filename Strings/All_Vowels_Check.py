print("\tPRINTING EVEN LENGTH WORDS IN STRING")
flg=1
while flg!=0 :
    s=input("\nEnter the larger STRING : ")
    vl=['a','e','i','o','u','A','E','I','O','U']
    vl_fl=[]
    for i in vl :
        if i in s:
            vl_fl.append(1)
        else :
            vl_fl.append(0)
    print("Vowels present : ",[vl[i] for i in range(len(vl)) if vl_fl[i]==1])
    print("Vowels not present : ",[vl[i] for i in range(len(vl)) if vl_fl[i]==0])
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
