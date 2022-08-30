print("\tEVEN NUMBERS IN A GIVEN RANGE :",end=" ")
st=1
while st>0 :
    A=[]
    st=int(input("\n\nEnter the Starting point(-1 to exit) : "))
    if st<0 :
        break
    end=int(input("Enter the Ending point : "))
    print("Even nos from {0} to {1} : ".format(st,end),[i for i in range(st,end+1) if i%2==0])
print("THE END")
