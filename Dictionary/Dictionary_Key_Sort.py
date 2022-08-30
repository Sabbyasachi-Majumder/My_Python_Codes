print("\tSORTING A DICTIONARY USING THE KEYS OR VALUES")
n=1
while True :
    c='a'
    while c != 'k' and c!='v' and c!='e':
        c=input("\nk for keys || v for values || e for exit  : ")
    if c=='e' :
        break
    n=int(input("Enter the no of terms (0 to exit) : "))
    if n==0 :
        break
    d={}
    for i in range(n) :
        key=input("Enter the {0}th key : ".format(i+1))
        value=input("Enter the {0}th value : ".format(i+1))
        d[key]=value
    print("Unsorted Dictionary : ",d)
    if c=='k' :    #Sorting acc to keys
        print("Sorted Dictionary acc to keys : ",end="")
        for i in sorted(d) :
            print(i+" : "+d[i]+" ; ",end="")
    else :           #Sorting acc to values
        print("Sorted Dictionary acc to values : ",end="")
        print(sorted(d.items(), key = lambda kv:(kv[1], kv[0])))
print("The End")
