teststr="Race car"
def is_palindrome(teststr):
    temp=teststr.lower()
    newstr =""
    for c in temp:
        if c.isalnum():
            newstr+=c
    reversestr =""
    strindx = len(newstr) 
    while(strindx>0):
        reversestr += newstr[strindx]
        strindx-=1
    if newstr == reversestr:
        print(True)
    else:
        print(False)
