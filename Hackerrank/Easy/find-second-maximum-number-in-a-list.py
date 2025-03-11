n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
runner_up = max(score for score in scores if score != max_score)
print(runner_up)
