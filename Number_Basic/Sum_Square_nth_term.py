print("\tSUM OF NUMBERS Nth TERM",end=" ")
n=2
while n>0 :
    n=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if n<1 :
        break
    s=0
    print(n,"th TERM SERIES :",end="")
    for i in range(1,n+1/) : 
        print(i,"*",i," + ",end="")
        s+=(i*i)
    print("\nSUM :",s)
print("THE END")
