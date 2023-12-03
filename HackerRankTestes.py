"""if __name__ == '__main__':
    python_students = []
    notaMinima = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students = [name, score]
        python_students.append(students)
        
        
    
    min_score = min(python_students, key=lambda x: float('inf') if isinstance(x[0], str) else x[1])[1]

    
    notaMinima = sorted(set(student[1] for student in python_students))[1]
    notaMinimaStudents = [student for student in python_students if student[1] == notaMinima]
    notaMinimaStudents.sort()
    for student in notaMinimaStudents: 
        print(student[0])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        input_data = input("")
        data = input_data.split()
        name = data[0]
        scores = list(map(float, data[1:]))
        student_marks[name] = scores

    query_name = input("")

    if query_name in student_marks:
        average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(f'{average_score:.2f}')
    else:
        print(f'Student {query_name} not find.')
        


if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        s = input().split()
        for i in range(1, len(s)):
            s[i] = int(s[i])
            
        if s[0] == "append":
            arr.append(s[1])
            
        elif s[0] == "insert":
            arr.insert(s[1], s[2])
        elif s[0] == "remove":
            arr.remove(s[1])
        elif s[0] == "pop":
            arr.pop()
        
        elif s[0] == "sort":
            arr.sort()
        elif s[0] == "reverse":
            arr.reverse()
        elif s[0] == "print":
            print(arr)

if __name__ == '__main__':
    arr = []
    N = int(input(""))
    for _ in range(N):
        command = input().split()
        if command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "reverse":
            arr.reverse()
        elif command[0] == "print":
            print(arr)


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))



"""    

