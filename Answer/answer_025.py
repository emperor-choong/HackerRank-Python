import os

def solve(s):
    result = s[0].upper() 
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i] != ' ':
            result = result + s[i].upper()
        else:
            result = result + s[i]

    return result

# There are 2 methods to run this code
# Method 1 : Set the environment variable for OUTPUT_PATH
# Method 2 : Uncomment the following line 
# os.environ["OUTPUT_PATH"] = "output.txt"
fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()