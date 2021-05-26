#prime numbers in given range
 
r = int(input("Enter upper range: "))  
  
for num in range(1,r + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)

"""
OUTPUT:
Enter upper range: 5
2
3
5
"""

