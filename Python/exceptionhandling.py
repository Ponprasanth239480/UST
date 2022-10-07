"""
import sys
try:
    print(100/0)
except:
    print(sys.exc_info()[1],"execption occured")
else:
    print("No execption occured")
finally:
    print("run this block of code always")
"""
"""
import sys
import os
try:
    os.remove("F:/python/test2.txt")
except:
    print(sys.exc_info()[1],"execption occured")
else:
    print("No execption occured")
finally:
    print("run this block of code always")
"""
"""
import os
try:
    x = int(input("enter first number: "))
    y = int(input("enter first number: "))
    print(x/y)
    #os.remove("F:/python/test2.txt")
except NameError:
    print("NameError execption occured")
except FileNotFoundError:
    print("FileNotFoundError execption occured")
except ZeroDivisionError:
    print("ZeroDivisionError execption occured")
    
import sys
try:
    x = int(input("enter first number: "))
    if x>50:
        raise ValueError(x)
except:
    print(sys.exc_info()[0])

x=-10
if x<0:
    raise Exception("no,number below zero is allowed")
x = "hello python"
if not type(x) is int:
    raise TypeError("only integers are allowed")
"""

try:
    a=90
    b="python"
    c=a/b
except TypeError:
    print("typeerror exception is occured")
try:
    mylist = [1,2,3,4,5]
    print(mylist[10])
except IndexError:
    print("IndexError exception is occured")
try:
    mydict = {'id':102,'name':'prasanth'}
    print(mydict['Name'])
except KeyError:
    print("KeyError exception is occured")

















