import math
print("sqr",math.sqrt(16))
print(math.pow(2,3)*2)
# exception handling
'''try:
    x=10/0
except:
    print("well that didn't work")'''

try:
    ans=input("num")
    num=int(ans)
    print(10/num)
except ZeroDivisionError as e:
    print("no 0")
except ValueError as e:
    print("not valid")
    print(e)
