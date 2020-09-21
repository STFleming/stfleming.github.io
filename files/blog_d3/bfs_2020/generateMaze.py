#!/usr/bin/python

import sys, getopt
import random

# gets the list of unvisited neighbours from the current node
def getUnvisitedNeighbours(x,y,vis,n):
    neighbours = []

    # check x
    if x == 0:
        if(not vis[x+1][y]):
            neighbours.append([x+1,y])
    elif x == (n-1):
        if(not vis[x-1][y]):
            neighbours.append([x-1,y])
    else:
        if(not vis[x+1][y]):
            neighbours.append([x+1,y])
        if(not vis[x-1][y]):
            neighbours.append([x-1,y])

    # check y 
    if y == 0:
        if(not vis[x][y+1]):
            neighbours.append([x,y+1])
    elif y == (n-1):
        if(not vis[x][y-1]):
            neighbours.append([x,y-1])
    else:
        if(not vis[x][y+1]):
            neighbours.append([x,y+1])
        if(not vis[x][y-1]):
            neighbours.append([x,y-1])

    return neighbours


# Used as the identifier for the generated vertex
def getIdent(x,y,n):
    return (x*n) + y


def main(argv):
    outputfile='graph.json'
    n=10
    try:
        opts, args = getopt.getopt(argv,"h:o:n",["outfile=", "nodes="])
    except getopt.GetoptError:
        print 'generateMaze.py -o <json graph> -n <n x n maze>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generateMaze.py -o <json graph> -n <n x n maze>'
            sys.exit()
        elif opt in ("-o", "--outfile"):
            outputfile = arg
        elif opt in ("-n", "--nodes"):
            n = int(arg)

    # Array of links
    links=[]

    # keep track of what has been visited
    visited=[];
    for x in range(n):
        visited.append([]);
        for y in range(n):
            visited[x].append(False);

    # recursively build the maze
    finished = False;
    stack = []  
    cell_x = 0
    cell_y = 0

    stack.append([cell_x, cell_y])
    while(not finished):
        # get the neighbours of the current cell 
        neigh = getUnvisitedNeighbours(cell_x,cell_y,visited,n)
        if not neigh:
            if not stack:
                finished = True # There is nothing on the stack end
            else:
                stackitem = stack.pop()
                cell_x = stackitem[0]
                cell_y = stackitem[1]
        else:
            # randomly select a neighbour
            selected = random.choice(neigh)
            visited[selected[0]][selected[1]] = True;
            stack.append(selected)
            src_id = getIdent(cell_x, cell_y,n)
            tgt_id = getIdent(selected[0], selected[1],n)
            connection = [src_id, tgt_id]
            links.append(connection)
            cell_x = selected[0]
            cell_y = selected[1]


    # render the JSON
    out = open(outputfile, "w")
    out.write("{\n")
    
    # render nodes 
    nodestr = "\"nodes\" : [" 
    for x in range(n):
        for y in range(n):
            nodestr += "\n{ \"id\": "+str(getIdent(x,y,n))+", \"name\": \"node"+str(getIdent(x,y,n))+"\"},"
    nodestr = nodestr[:-1] # remove the final comma
    nodestr += "\n]," 
    out.write(nodestr)

    # render links
    linkstr = "\"links\" : ["
    for l in links:
        linkstr += "\n{ \"source\": "+str(l[0])+", \"target\": "+str(l[1])+"},"
    linkstr = linkstr[:-1]
    linkstr += "\n]" 
    out.write(linkstr)

    out.write("}\n");
    out.close()

if __name__ == "__main__":
    main(sys.argv[1:])
