"""
Binary Equivalent
Problem Description
Mr. Binary is lost and wants to be found but the problem is he understands
only binary. His house is located at a maximum binary equivalence possible,
from the given set of numbers. A set is a binary equivalence if the number of
0 zeros and ones from a set of number are equal.

Constraints
1 <= N <= 20

1 <= Arr[i] <= 10^5, where Arr[i] is the ith element in the set of N numbers
in second line of input

Arr[i] will be unique

Input
First line contains N denoting the number of decimal numbers

Next line contains N space separated decimal numbers

Output
Single line output printing possible binary equivalence where number of digits
in this number is equal to number of bits present in the largest element in second
line of input. If there is no set which has binary equivalence then return 0 padded
to number of bits present in the largest element in second line of input.

Time Limit
1


Examples
Example 1

Input

3

2 7 10

Output

0011

Explanation

2 -> 0010 - 1's = 1, 0's = 3

7 -> 0111 - 1's = 3, 0's = 1

10 -> 1010 - 1's = 2, 0's = 2

Here we have taken up to 4 bits because the maximum number is 10 which needs 4
bits to be represented in binary. The number of zeroes and ones across the set is, 6
each. Hence, the set of [2,7,10] has binary equivalence. Similarly, if you consider
set[2,7], it also has binary equivalence, 4 each. But set [7,10] does not have binary
equivalence. Likewise, set[10] has binary equivalence of 2 each.

Total number of unique sets where binary equivalence is possible from all combinations
are 3 viz. Sets are [2,7,10], [2,7] and [10] which is the final answer. But as Mr. Binary
only understands zeroes and ones, return the binary of 3.

Since 10 is the largest element in the input on line 2, the number of bits required to represent
10 in binary is 4. Hence output needs to be padded upto 4 digits. Since binary of 3
represented as a 4-digit number is 0011, the answer is 0011

Note

Do not consider empty subset

Example 2

Input

1

7

Output

000

Explanation

7 -> 111 - 1's = 3, 0's = 1

Since there is only one element in the set and it also does not have binary equivalence, the
answer is 0. However, keeping output specifications in mind, the answer should be printed
as 000 since the highest element in second line of input viz. 7 has 3 bits when represented in
binary format.
"""

from itertools import combinations
import time
print("\tBINARY EQUIVALENCE")
n=1
while n>0 :
    n=int(input("\nEnter the no of terms (0 to exit): "))
    if n==0 :
        break
    s=0
    c=0
    v=[]
    print("Enter the elements  : ")
    for i in range(n):
        v.append(int(input("Enter {0}th term : ".format(i+1))))
    st=time.time()
    mlen=len(bin(max(v)).replace("0b",""))
    l=[]
    for i in range(1,n+1):
        l.append(list(combinations(v,i)))
    for i in l:
        for k in i :
            s=0
            for j in k :
                b=bin(j).replace("0b","")
                s+=(b.count("1")-(mlen-b.count("1")))
            if s==0 :
                c+=1
    print("Answer  in Decimal : ",c)
    cc=bin(c).replace("0b","")
    while len(cc)<mlen :
        cc="0"+cc
    print("Answer in Binary :",cc)
    en=time.time()
    print("Run Time : ",(en-st))
print("The End")



