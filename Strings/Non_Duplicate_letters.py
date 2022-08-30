print("\tPRINTING STRING WITHOUT DUPLICATES")
flg=1
while flg!=0 :
    s=input("\nEnter the STRING : ")
    ns=""
    for i in range(len(s)):
        if s[i] not in s[:i]+s[i+1:] and s[i] not in ns:
            ns+=s[i]
    if len(ns)>0 :
        print("String without duplicates are :",ns)
    else :
        print("No single words found .")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
