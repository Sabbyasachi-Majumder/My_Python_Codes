def order(x):
   n=0
   while x!=0:
       n = n+1
       x = x//10
   return n

print("\tARMSTRONG NUMBER : ")
n=1
while n!=0 :
    n=int(input("\nEnter the NUMBER (0 for exit ) : "))
    if n==0 :
        break
    ncpy=n
    s=0
    print(order(n))
    while ncpy>0 :
        s+=pow((ncpy%10),order(n))
        ncpy//=10
    if s==n:
        print("{0} is an Armstrong Number ".format(n))
    else :
        print("{0} is not an Armstrong Number ".format(n))
print("The End")
