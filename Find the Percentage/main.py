if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_student = list(student_marks[query_name])
    addition = sum(list_student)
    result = addition / len(list_student)
    print('%.2f'% result)
