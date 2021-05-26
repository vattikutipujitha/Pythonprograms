#factors
num = input("Enter a number: ");
count = 0;
number = int(num);
for i in range(2, number-1):
    if number%i == 0:
    	print(i);
    	i += 1;
    	count += 1;
if count==0:
    print("1",number);

"""OUTPUT:
Enter a number: 8
2
4
"""
