import re
print("\tSUBSTRING IN STRING CHECK")
flg=1
while flg!=0 :
    ls=input("\nEnter the larger STRING : ")
    ss=input("\nEnter the smaller STRING : ")
    if len(ss)>len(ls):
        print("Length of smaller string more than larger string length .Try again .")
    else :
        print("Given LARGER String : "+ls)
        print("Given SMALLER String : "+ss)
        if re.search(ss,ls) :
            print(ss+" is in "+ls)
        else :
            print(ss+" is not in "+ls) 
    flg=int(input("\nWant to continue (1-->YES | 0-->NO : "))
print("The End")
