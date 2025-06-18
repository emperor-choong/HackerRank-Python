s = input()

lower = False
for i in range(len(s)):
   for j in range(97, 123):
       if s[i] == chr(j):
           lower = True
           break
       
upper = False
for i in range(len(s)):
   for j in range(65, 91):
       if s[i] == chr(j):
           upper = True
           break
       
digit = False
for i in range(len(s)):
   for j in range(0, 10):
       if s[i] == str(j):
           digit = True
           break

# 1st Line
if lower or upper or digit:
    print(True)
else:
    print(False)

# 2nd Line
if lower or upper:
    print(True)
else:
    print(False)

# 3rd Line
print(digit)

# 4th Line
print(lower)

# 5th Line
print(upper)

