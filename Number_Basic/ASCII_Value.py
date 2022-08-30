print("\tASCII VALUE OF GIVEN LETTER",end=" ")
l=' '
while l!='+' :
    l=input("\n\nEnter the LETTER (+ to exit) : ")
    if l=='+' :
        break
    print("ASCII value of "+l+" : ",ord(l))
print("THE END")
