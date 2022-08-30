# 1 NAME , 4  ASSIGNMENT MARKS , 2 TEST MARKS , 2 LAB MARKS
import time
def inp_mks(n) :
    l=[]
    for i in range(n):
        l.append(int(input("Enter {0}th marks : ".format(i+1))))
    return l

def Grad(n) :
    if n>=90 :
        return "A"
    elif n>=80 :
        return "B"
    elif n>=70 :
        return "C"
    elif n>=60 :
        return "D"
    else :
        return "E"

def inp() :
    d={}
    d["name"]=input("Enter the name : ")
    print("\nEnter the 4 Assignment Marks : ")
    d["Am"]=inp_mks(4)
    print("\nEnter the 2 Test Marks : ")
    d["Tm"]=inp_mks(2)
    print("\nEnter the 2  Lab Marks : ")
    d["Lm"]=inp_mks(2)
    d["Av"]=(0.1*sum(d["Am"]))/2+(0.7*sum(d["Tm"]))/4+(0.2*sum(d["Lm"]))/2
    d["Gd"]=Grad(d["Av"])
    return d

print("\tCALCULATING AND GRADING MARKS OF STUDENTS")
n=1
while True :
    n=int(input("\nEnter the no of STUDENTS (0 to exit) : "))
    if n==0 :
        break
    L=[]
    print("\nEnter details of STUDENTS :")
    for i in range(n) :
        print("\nStudent No ",(i+1)," : ")
        L.append(inp())
    st=time.time()
    print("\nThe RESULTS are : ")
    c=1
    for i in L :
        print("\nStudent No : ",c)
        print("Name : "+i['name'])
        print("Assignment Marks : ",end="")
        for k in i['Am'] :
            print(k," , ",end="")
        print("\nTest Marks : ",end="")
        for k in i['Tm'] :
            print(k," , ",end="")
        print("\nLab Marks : ",end="")
        for k in i['Lm'] :
           print(k," , ",end="")
        print("\nAverage Marks : ",i['Av'],"\tGrade : "+i['Gd'])
        print("*"*50,end="")    
        c+=1
    en=time.time()
    print("\nTime ; ",(en-st))
print("The End")
