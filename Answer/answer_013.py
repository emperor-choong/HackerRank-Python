# At the time of writing, the output of this code doesn't match the expected output.
# Try use Python 2 instead of Python 3.

n = int(input())
string_list = input().split()  
t = tuple(map(int, string_list))

print(hash(t))  