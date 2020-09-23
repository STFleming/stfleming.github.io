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

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_small_tree/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

layer-by-layer: requires a queue
=======

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/queue/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>


queues can grow large
=======

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_tree/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_random_l1/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_random_l4/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

Solving shortest path
========

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_queue_small_shortest_path/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="650" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_small_maze/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/bfs_random_shortest_path/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="950" frameBorder="0"></iframe>

