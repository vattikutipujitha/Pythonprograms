#Random Module
>>> import random
>>> print(random.random())
0.5482647272863419 # float number between 0.0 to 1.0

>>>random.randint(10,20)
18

>>> l=[10,30,20,40,50]
>>> random.choice(l)
30

>>> random.shuffle(l)
>>> l
[30, 50, 20, 40, 10]

>>> random.randrange(100,1000,3)
214

>>> random.choices(l,weights=[2,3,4,5,6],k=4)
[20, 20, 10, 50]

>>> random.choices(l,k=4)
[10, 50, 50, 50]
