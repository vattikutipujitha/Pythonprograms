#Demonstrate raise block
try:
    raise IndexError
except IndexError:
    print("Index Bound of Exception")
except ZeroDivisionError:
    print("Zero Division Exception")
else:
    print("No Exception Occured")

"""
OUTPUT:
Index Bound of Exception
"""
