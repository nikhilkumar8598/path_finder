"""
Path Finding algorithm for multiple destinations for a fruit plucking line following robot. 
Note: Here we are assumimg that the trees bearing fruit are not placed exactly on the node. 
Instead, they are placed in the square gap enclosed by four nodes very close to one of the 
nodes.Once a node near which a tree is present is reached the Pluck fruit command 'P'
is sent to the firebird 5 robot which rotates clockwise until the camera encounters a fruit 
image and then plucks the fruit via a series of arm movements as per code in embedded c on 
the bot and continues.The last destination given by the user  must be the dump node. 
Note: All indices entered by a user must be in the following format:
rowcolumn,ex: to enter the position at which row=2 and column=1,just enter 21.
-Nikhil Kumar
"""
def pathfind(spos,dest,matr,n):
#Function that returns the directions to be followed for the least-cost path
    dir=[]#List to hold the sequence of directions for a particular cost matrix
    i=int(dest/10)#Extracting the indices of the passed destination position
    j=int(dest%10)
    currij=int(dest)#Setting the current indices to destination
    while(currij!=spos):#Traversing back upto starting position
        if((i-1)>=0 and (i-1)<n and (matr[i-1][j]==matr[i][j]-1)):
            dir.append("S")#S-South
            currij=int(str(i-1)+str(j))#Setting the current index
            i=i-1
        else:
            if((j+1)>=0 and (j+1)<n and (matr[i][j+1]==matr[i][j]-1)):
                dir.append("W")#W-West
                currij=int(str(i)+str(j+1))
                j=j+1
            else:
                if((i+1)>=0 and (i+1)<n and (matr[i+1][j]==matr[i][j]-1)):
                    dir.append("N")#N-North
                    currij=int(str(i+1)+str(j))
                    i=i+1
                else:
                    if((j-1)>=0 and (j-1)<n and (matr[i][j-1]==matr[i][j]-1)):
                        dir.append("E")#E-East
                        currij=int(str(i)+str(j-1))
                        j=j-1
                    else:
                        pass
        
    return (dir[::-1]+["P"])#Reversing the directions and adding P- Pluck fruit
def gen_cost_mat():                
# Function to calculate the square cost matrix for the given scenario
    r=int(input("Enter the no. of rows and columns in the square arena"))
    s=int(input("Enter the starting point \n"))
    while(1):
        if(int(s/10)>=r or int(s%10)>=r):
            print("Error: Invalid Index")
            s=int(input("Enter the starting point \n"))
        else:
            break
    n=int(input("Enter the no. of destinations \n"))
    while(1):
        if(n >= (r*r)-1):
            print("Error: These many destinations are not possible")
            n=int(input("Enter the no. of destinations \n"))
        else:
            break
    d=[] #List to store all the destinations
    dist=[] #List to to store the distances from the start to a particular destination
    findir=[] #List to store the node-wise navigation directions
    mat = [[0 for j in range(r)] for i in range(r)]
    #mat- Generated Cost 2d-list for a specific start-destination pair 
    i=0
    while(i<n):
        ip=int(input("Enter destination"))
        if(int(ip/10)>=r or int(ip%10)>=r):
            print("Error: Invalid Index")
        else:
            d.append(ip)# Appending the user entered destinations to the d matrix
            i+=1
        
    for i in range(n):
        for i in range(len(d)):
            dist.append(abs(int(s/10)-int(d[i]/10))+abs((s%10)-(d[i]%10)))
            #Calculating the distance between the start and destination positions
        minn=dist[0]
        minind=0 
        for i in range(1,len(dist)):#finding the next destination with least cost/distance
            if(dist[i]<minn):
                minn=dist[i]
                minind=dist.index(minn)
        for k in range(0,r):#generating the cost matrix
            for l in range(0,r):
                mat[k][l]=abs(int(s/10)-int(int(str(k)+str(l))/10))+abs(int(s%10)-int(int(str(k)+str(l))%10))
        #passing on the matrix to the pathfind function to obtain the optimal path
        findir=findir+(pathfind(s,d[minind],mat,r))   
        #store the path in a list and append all subsequent paths
        s=d[minind]
        d.remove(d[minind])
        dist=[]
       
    return(findir[0:len(findir)-1:1]+["D"]) #D- Dump all the fruits
def main():
    print(gen_cost_mat())
if __name__== "__main__":
  main()       