#Demonstrate custom exception/user defined exception
n=int(input("Enter Number:"))
if(n<0):
   raise Exception("Raised an Exception")
else:
    print("No Exception Occured")

"""
OUTPUT:

Enter Number2
No Exception Occured

Enter Number:-1
Traceback (most recent call last):
  File "C:/Users/v.suresh babu/OneDrive/Documents/2-2/TS/PFSD Sessions/Module 1/Program71.py", line 4, in <module>
    raise Exception("Raised an Exception")
Exception: Raised an Exception

"""
