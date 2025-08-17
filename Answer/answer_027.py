def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i+k]
        temp = []
        for char in t:
            if char not in temp:
                temp.append(char)
        u = "".join(temp)
        print(u)

string, k = input(), int(input())
merge_the_tools(string, k)