#!/usr/bin/python

import sys, getopt
import random
import math

def main(argv):
    outputfile = ''
    numnodes = 10
    degree = 2
    locality = 10 
    try:
        opts, args = getopt.getopt(argv,"h:o:n:d:l",["ofile=", "nodes=", "degree=", "locality="])
    except getopt.GetoptError:
        print 'generateRandom_xy.py -o <outputfile> --nodes=<number of nodes in one dimension> --degree=<degree of the graph> --locality=<how close are connections to each other>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generateRandom.py -o <outputfile> --nodes=<number of nodes in one dimension> --degree=<degree of the graph> --locality=<how close are connections to each other>'
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--nodes"):
            numnodes = int(arg)
        elif opt in ("-d", "--degree"):
            degree = int(arg)
        elif opt in ("-l", "--locality"):
            locality = int(arg)

    # 2D array of nodes
    nodes=[]

    # Array of links
    links=[]

    # populate the nodes
    current_id = 0
    for i in range(numnodes):
        nodes.append([])
        for j in range(numnodes):
            nodes[i].append([j,i])

    for nline in nodes:
        for n in nline: 
            for d in range(random.randint(1,degree)):
                target_x = n[0]+random.randint(0, locality)
                target_y = n[1]+random.randint(0, locality)
                while(math.sqrt( (target_x * n[0]) + (target_y * n[1])) > locality):
                    target_x = n[0]+random.randint(0, locality)
                    target_y = n[1]+random.randint(0, locality)
                target_node = nodes[target_x][target_y]
                connection = [n, target_node]
                links.append(connection)

    # render the JSON
    out = open(outputfile, "w")
    out.write("{\n")
    
    # render nodes 
    nodestr = "\"nodes\" : [" 
    for nlist in nodes:
        for n in nlist:
            nodestr += "\n{ \"id\": \""+str(n[0])+"_"+str(n[1])+"\", \"name\": \"node_"+str(n[0])+"_"+str(n[1])+"\"},"
    nodestr = nodestr[:-1] # remove the final comma
    nodestr += "\n]," 
    out.write(nodestr)

    # render links
    linkstr = "\"links\" : ["
    for l in links:
        linkstr += "\n{ \"source\": \"node_"+str(l[0][0])+"_"+str(l[0][1])+"\", \"target\": \"node_"+str(l[1][0])+"_"+str(l[1][1])+"\"},"
    linkstr = linkstr[:-1]
    linkstr += "\n]" 
    out.write(linkstr)

    out.write("}\n");
    out.close()

if __name__ == "__main__":
    main(sys.argv[1:])
