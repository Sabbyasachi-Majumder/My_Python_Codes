print("\tBINARY STRING CHECKER")
flg=1
while flg!=0 :
    s=input("\nEnter the  STRING : ")
    if s.count('0')+s.count('1')==len(s):
        print(s+" is a BINARY STRING")
    else :
        print(s+" is not a BINARY STRING")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
