# reads and runs tank runner format
import sys
filename = sys.argv[1]
f = open(filename, "r")
commands = f.readlines()

def findAction(x):
    if x == "w":
        return "forward"
    elif x == "s":
        return "backward"
    elif x == "a":
        return "turn left"
    elif x == "d":
        return "turn right"


for command in commands:
    if command[0] == "#":
        print(command.strip())
    
    else:
        action = findAction(command[0])
        print(action)
        #we could use <print(findAction(command[0]))>, but i have later use for action
        