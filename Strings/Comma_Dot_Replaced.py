print("\tREPLACE DOTS WITH COMMAS AND VICE VERSA")
flg=1
while flg!=0 :
    s=input("\nEnter the 1st STRING : ")
    s2=''
    for i in s :
        if i==',':
            s2+='.'
            continue
        if i=='.' :
            s2+=','
            continue
        s2+=i
    print("Replaced String :"+s2)
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
