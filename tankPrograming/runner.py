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
        speed = command[2]
        timeAt = 4
        
        if command[3] != " ":
            speed += command[3]
            timeAt += 1
            if command[4] != " ":
                speed += command[4]
                timeAt += 1
                
        time = command[timeAt]
        timeAt += 1
        
        while command[timeAt] != " ":
             timeAt += 1
             time += command[timeAt]
            
        print(action + " at " + speed + " for " + time)
        
        