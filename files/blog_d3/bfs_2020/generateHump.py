#!/usr/bin/python

import sys, getopt

def main(argv):
    outputfile = ''
    levels = 0 
    degree = 2
    try:
        opts, args = getopt.getopt(argv,"h:o:l:d",["ofile=", "levels=", "degree="])
    except getopt.GetoptError:
        print 'generateTree.py -o <outputfile> --levels=<levels of the tree> --degree=<degree of the graph>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generateTree.py -o <outputfile> --levels=<levels of the tree> --degree=<degree of the graph>'
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-l", "--levels"):
            levels = int(arg)
        elif opt in ("-d", "--degree"):
            degree = int(arg)

    nodes=[]
    links=[]

    # populate the nodes
    current_id = 0
    for i in range(levels):
        clevel = []
        for j in range(degree**i):
            clevel.append(current_id)
            current_id = current_id + 1
        nodes.append(clevel)

    # come down the other side of the hump
    for i in reversed(range(levels-1)):
        clevel=[]
        for j in reversed(range(degree**i)):
            clevel.append(current_id)
            current_id = current_id + 1
        nodes.append(clevel)

    # populate the links
    current_link_id = 0
    current_link_next_level = 0;
    for i in range(levels-1):
        current_link_next_level = current_link_id + degree**i
        for j in range(degree**i):
            for k in range(degree):
                connection = [current_link_id, current_link_next_level]       
                links.append(connection)
                current_link_next_level = current_link_next_level + 1
            current_link_id = current_link_id + 1

    current_link_id = current_link_next_level; 
    # opposite direction for coming down the hump
    current_link_prev_level = 0
    for i in reversed(range(levels-1)):
        current_link_prev_level = current_link_id - degree**(i+1)
        for j in range(degree**i):
            for k in range(degree):
                connection = [current_link_id, current_link_prev_level]
                links.append(connection)
                current_link_prev_level = current_link_prev_level + 1
            current_link_id = current_link_id + 1

    # render the JSON
    out = open(outputfile, "w")
    out.write("{\n")
    
    # render nodes 
    nodestr = "\"nodes\" : [" 
    for level in nodes:
        for n in level:
            nodestr += "\n{ \"id\": "+str(n)+", \"name\": \"node"+str(n)+"\"},"
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
