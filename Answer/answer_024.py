def print_rangoli(size):
    width = size*2-1 + size*2-2

    left = ""
    right = ""
    for i in range(97+size-1, 97-1, -1):
        result = left + chr(i) + right
        print(result.center(width, '-'))

        left = left + chr(i) + '-' 
        right = '-' + chr(i) + right

    for i in range(97+1, 97+size):
        left = ""
        right = ""
        result = ""
        for j in range(i+1, 97+size):
            left = chr(j) + '-' + left
            right = right + '-' + chr(j) 

        result = left + chr(i) + right
        print(result.center(width, '-'))
        
n = int(input())
print_rangoli(n)

