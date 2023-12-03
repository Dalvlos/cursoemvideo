import random
n1 = str(input("First student: "))
n2 = str(input("Second student: "))
n3 = str(input("Third student: "))
n4 = str(input("Forth student: "))
listone = [n1, n2, n3, n4]
ChooseSequence = random.shuffle(listone)
print("The student sequence chosen is")
print(listone)

"""from random import shuffle
n1 = str(input("First student: "))
n2 = str(input("Second student: "))
n3 = str(input("Third student: "))
n4 = str(input("Forth student: "))
listone = [n1, n2, n3, n4]
ChooseSequence = shuffle(listone)
print("The student sequence chosen is")
print(listone)"""