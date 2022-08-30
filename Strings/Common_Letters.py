print("\tPRINTING COMMON LETTERS IN BOTH STRINGS")
flg=1
while flg!=0 :
    s1=input("\nEnter the 1st STRING : ")
    s2=input("\nEnter the 2nd STRING : ")
    s3=""
    for i in s1:
        if i in s2 and i not in s3:
            s3+=i
    if len(s3)>0 :
        print("common words : "+s3)
    else :
        print("No single words found .")        
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
