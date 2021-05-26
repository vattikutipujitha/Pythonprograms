a=int(input("Enter First Value"))
b=int(input("Enter Second Value"))
c=int(input("Enter Third Value"))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
else:
    if b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")
