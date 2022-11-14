while True:
    dim_n = input("Please give space dimension of n :")
    try:       #Check Positive Integer Number
        dim_n = int(dim_n)
        if dim_n >= 0:
            break
        else:
            print("Please type a positive integer. ")
        break
    except ValueError:
        print("Please type a positive integer. ")
print(f"\nThe robot will move in a scale of: {dim_n} x  {dim_n} (0...{dim_n-1}, 0...,{dim_n-1}). Starting position is: (0,0)")
#Variables
command = "s"
x = 0
y = 0
new_movement_x = 0
new_movement_y = 0
#MOVEMENT_COMMAND
while command != " ":
    command = input("\nPlease give movement command(up-down-right-left, e.g-u2) or a blank character to exit the program: ")
    if not command:
        continue
    movement = command[0].lower()
    #Movement-Defensive Programming
    if movement not in ["u", "d", "l", "r"]:
        continue
    number = int(command[1:])
    if movement == "u":
        new_movement_x = x - number
    elif movement == "d":
        new_movement_x = x + number
    elif movement == "l":
        new_movement_y = y - number
    elif movement == "r":
        new_movement_y = y + number
    x = new_movement_x
    y = new_movement_y
    #OUT OF LIMITS COMMANDS
    if x > dim_n or x <0 or y > dim_n or y <0:
        print("\nERROR!! It's outside the boundaries of the area!Try again.")
        print(f"\nRobot's new position is: {x},{y}")
    else:
        print(f"\nRobot's new position is: {x},{y}")        
print("\n\nExit Game...")