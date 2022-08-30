print("\tSTAR PATTERN")
while True :
    n=int(input("\nEnter the no of lines (0 to exit) : "))
    if n==0 :
        break
    print("N : ",n)
    for i in range (n, 0, -1):
        print((n-i) * '  ' + i * '*') 
print("The End")
