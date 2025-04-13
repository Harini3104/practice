 #local and global variable
mystr="My Name is"
print(mystr)

def sfunc():
    global mystr
    mystr="Harini"
    print(mystr)
sfunc()
print(mystr)

