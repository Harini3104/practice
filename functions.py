 #define a function
def func1():
   print("i am harini")
func1()
print(func1())
print(func1)
#function that takes arg
def func2(arg1,arg2):
      print(arg1,"",arg2)
#function that return values
def cube(c):
   return c*c*c
func2(12,13)
print(cube(3))
#function with default val arg
def pow(x,y=1):
    res=1;
    for i in range(y):
        res=res*x
    return res
print(pow(2))
print(pow(2,3))
print(pow(y=3,x=2))
#function with variable no of arg
def multi_add(*args):
    res=0
    for x in args:
        res=res+x
    return res
print(multi_add(1,2,3,4,5))
