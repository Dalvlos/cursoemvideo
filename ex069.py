"""

Crie um programa que leia a idade e o sexo de varios pessoas.
A cada pessoa cadastrada o programa devera perguntar se o usuario
quer ou nao continuar. No final mostre:

a - quantas pessoas tem mais de 18 anos.
b- Quantos homens foram cadastrados.
c- Quantas mulheres tem menos de 20 anos.

"""
data = []
control = True
while control:
    
    name = str(input("Name: ")).upper()
    age = int(input("Age: "))
    gender = str(input("Gender: ")).upper()
    
    userRegistration = {
        "name" : name,
        "age" : age,
        "gender" : gender,
    }

    data.append(userRegistration)

    keepInsertData = str(input("Do you wanna insert new data? Press y/n ")).lower()
    if keepInsertData.lower() == "n":
        control = False

for userRegistration in data:
    print(userRegistration)

counterMen = 0
counterAge = 0
counterWomanLess20 = 0

for item in data:
    genders = item.get("gender", " ").lower()
    if genders == "male":
        counterMen += 1

    ages = item.get("age", " ")
    if ages >= 18:
        counterAge += 1

    ageGender = {'idade': item.get("age"), 'genero': item.get("gender")}
    if ageGender['genero'].lower() == "female" and ageGender['idade'] <= 20:
        counterWomanLess20 += 1


print(f"There is {counterAge} people over 18 registered.")
print(f"There is {counterMen} men registered.")
print(f"There is {counterWomanLess20} women less than 20 years old.")
