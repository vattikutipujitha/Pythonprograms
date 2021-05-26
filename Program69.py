#demonstrate finally keyword
try:
    l=[10,20,30,40,50]
    #print(l[2])
    print(l[5])
except IndexError:
    print("Index Bound of Exception")
finally:
    print("End of Program")

"""
OUTPUT:
30
End of Program

Index Bound of Exception
End of Program

"""
