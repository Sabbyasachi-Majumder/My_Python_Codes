print("\tORDER OF A NUMBER : ")
n=1
while n!=-1 :
    n=int(input("\nEnter the NUMBER (-1 for exit ) : "))
    if n==-1 :
        break
    ncpy=n
    o=0
    if n==0 :
        print("ORDER : 1")
        continue
    while ncpy>0:
        o+=1
        ncpy=ncpy//10
    print("ORDER : ",o)
print("The End")
