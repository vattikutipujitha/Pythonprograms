#demonstrate variable length arguments
def add(*x):
    total=0
    for n in x:
        total=total+n
    print(total)
add(10,20,30,40,50)
