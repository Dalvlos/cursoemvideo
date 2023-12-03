"""if __name__ == '__main__':
    while True:
        n = int(input().strip())
        while n >= 0 or n <= 100:
            
            if n == 1 or n == 3:
                print('Weird')
            elif n == 2 or n == 4 or n == 5:
                print('Not Weird')
            elif n >= 6 and n <= 20:
                print('Weird')
            else:
                print('Not Weird')
            break
        


if __name__ == '__main__':
    while True:
        a = int(input())
        b = int(input())
        if a < 1 and a < a** 10 and b < 1 and b < b** 10:
            print(a+b)
            print(a-b)
            print(a*b)
        break



if __name__ == '__main__':
    n = int(input())
    a = n - 1
    limite = a * a
    c = 0
    d = 0
    print(c)
    while d < limite:
        c += 1
        d = c * c
        print(d)



if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        i += 1
        print(i, end='')
        
        


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    entrada_usuario = [x, y, z, n]


    saida = [[i, j, k] for i in range(entrada_usuario[0] + 1)
                      for j in range(entrada_usuario[1] + 1)
                      for k in range(entrada_usuario[2] + 1) if i + j + k != 2]

    print(saida)

Resposta correta:
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k!=n):
                    l.append([i,j,k])
    print(l)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = max(arr)
    c = arr.count(a)
    for i in range(c):
        arr.remove(a)
    print(max(arr))
    
"""
if __name__ == '__main__':
    python_students = []
    notaMinima = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students = [name, score]
        python_students.append(students)
        
        
    
    min_score = min(python_students, key=lambda x: float('inf') if isinstance(x[0], str) else x[1])[1]

    
    notaMinima = [student for student in python_students if student[1] == min_score]
    notaMinima.sort()
    for student in notaMinima:
        print(student)
    
    print(python_students)