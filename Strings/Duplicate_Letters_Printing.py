print("\tDUPLICATE LETTERS IN STRING")
flg=1
while flg!=0 :
    s=input("\nEnter the STRING : ")
    ds=''
    d=[]
    for i in s:
        if s.count(i)>1 and i not in d :
            ds+=i+' '
            d.append(i)
    if ds :
        print("Duplicate letters : "+ds)
    else :
        print("There are no duplicate letters in the string .")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
