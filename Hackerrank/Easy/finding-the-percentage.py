n = int(input())
student_marks = {}
for _ in range(n):
    name, *scores = input().split()
    student_marks[name] = list(map(float, scores))

query_name = input()
scores = student_marks[query_name]
average = sum(scores) / len(scores)
print(f"{average:.2f}")
