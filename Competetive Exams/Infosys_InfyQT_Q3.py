import time
A=78
B=13
C=78
D=1
N=15
i=0
e=0
i=time.time()
m=1000000007

if N == 0 :
    print((A*B)%m)
else :
    if A-C <= N :
        x=C
        if B-D <= N :
            y=D
        else :
            y=B-N
    else :
        x=A-N
    print((x*y)%m)
e=time.time()
print(e-i)
