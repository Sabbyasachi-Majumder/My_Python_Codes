from difflib import get_close_matches
print("\tPRINT LOSE MATCHES OF A WORD")
flg=1
while flg!=0 :
    W=[]
    flg=int(input("Enter no of terms : "))
    print("Enter th words : ")
    for i in range(flg):
        W.append(input("Enter {0}th terrm : ".format(i+1)))
    s=input("\nEnter the  STRING to be matched : ")
    if get_close_matches(s,W) :
        print("Similar words to {0} : ".format(s),get_close_matches(s,W))
    else :
        print("No similar words or close to similar found . ")
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
