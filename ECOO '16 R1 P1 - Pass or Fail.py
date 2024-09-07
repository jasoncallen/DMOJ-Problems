student_list = {}
for i in range(10):
    weights = input().split()
    test_weight = int(weights[0])
    assignment_weight = int(weights[1])
    projects_weight = int(weights[2])
    quiz_weight = int(weights[3])
    students = int(input())
    pass_list = 0
    for s in range(students):
        student_list[s] = input().split()
        tests = int(student_list[s][0])
        assignments = int(student_list[s][1])
        projects = int(student_list[s][2])
        quizzes = int(student_list[s][3])

        if ((test_weight * tests) + (assignment_weight * assignments) + (projects_weight * projects) + (quiz_weight * quizzes)) >= 5000:
            pass_list +=1
    print(pass_list)