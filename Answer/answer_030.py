from itertools import permutations

S, k = input().split()
k = int(k)

result = list(permutations(S, k))
result.sort()
for x in result:
    print("".join(x))