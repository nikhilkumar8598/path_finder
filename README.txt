This is path finding algorithm for multiple destinations.This was used for a fruit plucking 
line following robot. 

Note: Here we are assumimg that the trees bearing fruit are not placed exactly on the node. 
Instead, they are placed in the square gap enclosed by four nodes very close to one of the 
nodes.Once a node near which a tree is present is reached the Pluck fruit command 'P'
is sent to the firebird 5 robot which rotates clockwise until the camera encounters a fruit 
image and then plucks the fruit via a series of arm movements as per code in embedded c on 
the bot and continues.The last destination given by the user  must be the dump node. 

Note: All indices entered by a user must be in the following format:
rowcolumn,ex: to enter the position at which row=2 and column=1,just enter 21.
-Nikhil Kumar
