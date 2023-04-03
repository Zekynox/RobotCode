# reads and runs tank runner format
import sys
filename = sys.argv[1]
f = open(filename, "r")
commands = f.readlines()
for command in commands:
    if command[0] == "#":
        print(command.strip())
    else:
        pass
