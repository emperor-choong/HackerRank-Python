n = int(input())
arr = map(int, input().split())

score = list(arr)
score.sort(reverse=True)

max = score[0]
for i in range(n):
    if score[i] < max:
        runner_up = score[i]
        break

print(runner_up)
