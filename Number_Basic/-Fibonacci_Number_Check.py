def fibonacci_check(a,b,x):
    if a+b== x:
        return a+b==x
    elif a+b<x :
        fibonacci_check(b,a+b,x)
    elif a+b>x :
        return a+b==x

print("\tFIBONACCI NUMBERS CHECK",end=" ")
n=2
while n>0 :
    n=int(input("\n\nEnter the NUMBER  (-1 to exit):"))
    if n<1 :
        break
    if fibonacci_check(-1,1,n) :
        print(n," is a Fibonacci Number")
    else :
        print(n," is not a Fibonacci Number")
print("THE END")
