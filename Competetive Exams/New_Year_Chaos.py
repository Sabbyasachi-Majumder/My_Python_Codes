"""
New Year Chaos
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of
people queued up, and each person wears a sticker indicating their initial position in the queue. Initial
positions increment by from at the front of the line to at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. If two people
swap positions, they still wear the same sticker denoting their original places in line. One person can bribe
at most two others. For example, if and bribes , the queue will look like this:
.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took
place to get the queue into its current state!
Function Description
Complete the function minimumBribes in the editor below. It must print an integer representing the
minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
minimumBribes has the following parameter(s):
q: an array of integers
Input Format
The first line contains an integer , the number of test cases.
Each of the next pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has space-separated integers describing the final state of the queue.
Constraints
Subtasks
For score
For score
Output Format
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print
Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than people.
Sample Input
2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output
3
Too chaotic
Explanation
Test Case 1
The initial state:
After person moves one position ahead by bribing person :
Now person moves another position ahead by bribing person :
And person moves one position ahead by bribing person :
So the final state is after three bribing operations.
Test Case 2
No person can bribe more than two people, so its not possible to achieve the input state.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q=[i-1 for i in q]
    b=0
    for i in range(len(q)) :
        if q[i]>i :
            if q[i]-i>2 :
                return "Too chaotic"
            b+=(q[i]-i)
    return b


if __name__ == '__main__':
    t = int(input())
    res=[]
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        res.append(minimumBribes(q))
    for i in range(len(res)) :
        print(res[i])

