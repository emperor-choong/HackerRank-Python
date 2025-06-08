records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

skor = []
for i, j in records:
    skor.append(j) 
 
lowest_score = min(skor) 

i = 0
while i < len(skor):
    if skor[i] == lowest_score:
        skor.remove(skor[i])
        continue
    i += 1

second_lowest_score = min(skor) 

nama = []
for i, j in records:
    if j == second_lowest_score:
        nama.append(i)

nama.sort()
for i in nama:
    print(i)

