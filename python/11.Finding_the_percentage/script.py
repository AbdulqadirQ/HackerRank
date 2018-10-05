n = int(input())
student_scores = {}
for _ in range(n):
    name, *line = input().split()
    average_score = sum(list(map(float, line)))/3
    student_scores[name] = average_score

print("{0:.2f}".format(student_scores[input()]))