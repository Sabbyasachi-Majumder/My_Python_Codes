print("\tSTRING PALLINDROME CHECK")
flg=1
while flg==1 :
    s=input("\nEnter the STRING : ")
    if s==s[::-1]:
        print(s+" is a pallindrome word")
    else:
        print(s+" is not a palindrome word")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
