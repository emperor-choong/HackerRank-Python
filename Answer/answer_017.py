def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    s = ''.join(l)
    return s

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)