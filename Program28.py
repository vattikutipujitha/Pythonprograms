#Divisors
n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)


"""
OUTPUT:
Enter an integer:9
The divisors of the number are:
1
3
9
"""
