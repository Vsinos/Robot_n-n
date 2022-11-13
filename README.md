# Robot_n*n
 Basic Program of robot moving around n*n space.

Write a program that simulates the movement of a robot with the following
specifications: The robot moves in a space of dimensions n x n, where dimension n will be given by the user at the beginning of the program and will be a positive integer. 
We consider coordinate system (x,y), where position (0,0) is top left and movement towards up decreases x, while down movement increases x. Accordingly, moving left decreases y and to the right increases y. 

A.  The initial position of the robot will be at (0, 0) and it can accept left movement commands, right, up or down (via the first character of each command l, r, u, d respectively). Every command movement is given along with an integer indicating how many steps to the specific one direction the robot should take (eg r1, u5, l3, d1).

B.  The user will continuously give move commands until an empty string is given as a command output.

C.  The program after each movement command will calculate its new current position
robot and will display it with a relevant message.

D.  If the user gives a movement command that cannot be executed, then the program will inform the user and request a new valid movement command. Movements that
cannot be performed are those that take the robot out of space, such as for
example at position (-20, 30) or (40, -90) but also at positions that have x coordinate
or y greater than or equal to n.
E.  To implement defensive programming so that valid values ​​are given by the user
for the dimension n of the space, as well as for the movement commands as far as the direction and the distance.