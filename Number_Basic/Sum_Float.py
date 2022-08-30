print("\t Sum of numbers :")
k=1
sum=0.0
s="T"
while s=="T":
    a=float(input("\nEnter the {0}th no : ".format(k)))
    sum+=a
    k+=1
    s=input("\nDo you want to continue ?(T/F) : ")

print("\nSum : {0}".format(sum))
