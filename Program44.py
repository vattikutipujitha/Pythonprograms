#fibanocci
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
x=int(input("Enter a number: "))
print(fib(x))
    
