questions = int(input())
student_ans = ""
for a in range(questions):
    student_ans = student_ans + input()

answers = ""
for a in range(questions):
    answers = answers + input()

correct = 0
for q in range(questions):
    if student_ans[q] == answers[q]:
        correct += 1

print(correct)