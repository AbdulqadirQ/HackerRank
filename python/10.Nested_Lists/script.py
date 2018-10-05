n = int(input())
scores = []
names = []
for grades in range(n):
    names.append(input())
    scores.append(float(input()))

second_lowest_score = sorted(list(set(scores)))[1]
low_students = []
for index, score in enumerate(scores):
    if score == second_lowest_score:
        low_students.append(names[index])
print('\n'.join(sorted(low_students)))

