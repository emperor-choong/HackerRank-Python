N = int(input())

commands = []
for _ in range(N):
    command = input()
    commands.append(command)

result = []
for command in commands:
    array = command.split()
    operation = array[0]
    if operation == "insert":
        i = int(array[1])
        e = int(array[2])
        result.insert(i, e)
    elif operation == "print":
        print(result)
    elif operation == "remove":
        e = int(array[1])
        result.remove(e)
    elif operation == "append":
        e = int(array[1])
        result.append(e)
    elif operation == "sort":
        result.sort()
    elif operation == "pop":
        result.pop()
    elif operation == "reverse":
        result.reverse()
        