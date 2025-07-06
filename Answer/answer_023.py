def print_formatted(number):
    width = len(bin(number))-2 #Remove "0b" that's why we subtract 2
    for i in range(1, number+1):
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

n = int(input())
print_formatted(n)