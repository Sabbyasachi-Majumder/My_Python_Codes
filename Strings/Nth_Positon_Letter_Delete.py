print("\tDELETING NTH POSITION LETTER IN A WORD")
flg=1
while flg!=0 :
    s=input("\nEnter the  STRING : ")
    w=s.split(' ')
    n=int(input("Enter the position : "))
    if n>len(s):
        print("Given position no out of length of string given . Try again")
    else :
        print("Letter at {0}th position is {1} and new word : ".format(n,s[n-1]),''.join([s[i] for i in range(len(s)) if  i!=n-1]))
    flg=int(input("\nWant to continue (1-->YES | 0-->NO) : "))
print("The End")
