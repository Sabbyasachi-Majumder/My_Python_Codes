def fibonacci(a,b,t):
    if t<1:
        print("")
    else:
        print(a+b," ;",end="")
        return fibonacci(b,a+b,t=t-1)

print("\tFIBONACCI NUMDERS TO GIVEN TERM",end=" ")
t=2
while t>0 :
    t=int(input("\n\nEnter the NUMBER of TERMS (0 to exit):"))
    if t<1 :
        break
    print(t,"th TERMS of Fibonacci nos :",end="")
    fibonacci(-1,1,t)
print("THE END")
