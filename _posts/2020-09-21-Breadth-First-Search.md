---
title: 'Breadth-First Search (BFS)'
date: 2020-09-21
permalink: /posts/2020/09/breadth-first-search/
tags:
  - teaching
  - graph traversal
  - algorithms
---

This post explains the breadth-first search graph traversal algorithm. It is full of interactive examples that I used as part of my lectureship application at Swansea University.     
                                                                                                 
Say we have a maze, and we want to find the shortest route from the entrance to the exit. We can encode that maze as a graph and use BFS to solve it. On the maze below, you can hit `play()` to see the algorithm explore the maze, shown in green. Notice how it flows through like water; whenever it reaches a fork, it explores all the possible paths simultaneously until it has explored the entire maze.

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/title_slide/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="630" frameBorder="0"></iframe>

After exploring the entire maze, the algorithm then uses information it gathered during its traversal to find the optimal shortest path to solve it, shown by the squiggly red line. **By the end of this post you will know how this simple algorithm can perform such a magical and vital task.**

layer-by-layer
=======
In the maze above, whenever the BFS encountered multiple possible directions, it started exploring all of them simultaneously. Thinking in a more graph representation what this means is that BFS explores the graph in a layer-by-layer fashion. 

Let's play with the tree example below. This tree is a directed graph, meaning that traversing edges can only happen in a specific direction, in this case from the root down to the leaves. Please select a starting node, on the graph by clicking on it. You can see that the node you selected is now active (orange) and all nodes directly reachable from it are being scheduled to be visited next (yellow). 

Now click the `step()` button to move to the next (coarse) step of the algorithm. All the previously active nodes (orange) are now marked as visited (green). And all the upcoming nodes (yellow) are now active. Keep clicking through until you can't go any further. 

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_tree_fixed_layout/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

BFS not only applies to directed graphs but undirected ones also, as shown in the example below. One thing to notice when playing with this example is that nodes are only visited once during the graph exploration.

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

layer-by-layer: requires a queue
=======

Zooming in on the algorithm we use a data structure, known as a queue, to achieve that layer-by-layer approach when traversing the entire graph. Queue data structures are much like a queue in the real world.  If you go to a bank, and it's a bit busy, you would join the end of a _hopefully_ socially distanced queue. When a teller becomes available the person at the front of the queue leaves it, and everyone else shuffles along. 

<iframe src="http://localhost:4000/files/blog_d3/bfs_2020/queue/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="250" frameBorder="0"></iframe>

We do the same thing in BFS with queue data structures, except instead of people we use it to schedule which nodes we still have to explore in our graph.  When we visit a node, we `enqueue()` all the neighbours of that node we have yet to explore. Once we have finished doing that we then `dequeue()` the node at the front of the queue to find out which node to explore next. 

Below we can see the queue in action on the previously shown undirected graph. Clicking a graph node will set it as the starting node, then `play()` will play through the algorithm, as `step()` will step through it. 

<iframe src="http://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

Notice that if a node has already been enqueued or already visited fully then we do not enqueue it again. In BFS we only visit each node once.

queues can grow large
=======

This queue data structure is useful for scheduling nodes that we want to visit. However, we should be careful. On the undirected tree graph below, select node 1 as the start node and hit `play()`. What happens to the queue as we get down to the leaves?

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_tree/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

The space complexity required for maintaining this queue can become quite large. To illustrate this point further I have two randomly generated graphs below. Each graph has the same number of nodes and edges, however, the topology is different. In Graph A the connections are much more local, as in Graph B edges are less local. 

graph A
==========
Select any node and hit `play()` notice how the queue grows.

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_random_l1/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

graph B
=========
Select any node and hit `play()` notice how the queue grows.

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_random_l4/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

Despite having the same number of edges and nodes, the queue size when applying BFS to each graph grows quite differently, with the max queue depth for graph B being far more significant. When using BFS, we need to be careful of the memory requirements, and the topology of the input graph.   

That is BFS; we are exploring a graph in a layer-by-layer fashion, using a queue data structure to schedule upcoming nodes to visit. But what about the maze at the top of this page, how can we use BFS to find the optimal shortest path?

Solving shortest path
========

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_small_shortest_path/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_small_maze/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_random_shortest_path/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

