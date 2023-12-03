import random
n1 = str(input("First student: "))
n2 = str(input("Second student: "))
n3 = str(input("Third student: "))
n4 = str(input("Forth student: "))
listone = [n1, n2, n3, n4]
Chooseoneofthose = random.choice(listone)
print("The student chosen was {}".format(Chooseoneofthose))

"""sumary_line

from random import choice
n1 = str(input("First student: "))
n2 = str(input("Second student: "))
n3 = str(input("Third student: "))
n4 = str(input("Forth student: "))
listone = [n1, n2, n3, n4]
Chooseoneofthose = choice(listone)
print("The student chosen was {}".format(Chooseoneofthose))"""



