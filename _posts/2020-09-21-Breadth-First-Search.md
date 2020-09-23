---
title: 'Breadth First Search (BFS)'
date: 2020-09-21
permalink: /posts/2020/09/breadth-first-search/
tags:
  - teaching
  - graph traversal
  - algorithms
---

This post explains the breadth first search algorithm. It is an interactive example that was used as part of my application to a lectureship at Swansea University.

Say we have a maze, and we want to find the shortest route from the entrance to the exit. We can use BFS to do this. On the maze below you can hit `play()` and see the algorithm explore the maze in green. Notice how it flows through the maze like water, whenever it reaches a fork it explores all the paths simulataneously until it has explored the entire maze. 

<iframe src="https://stfleming.github.io/files/blog_d3/bfs_2020/title_slide/index.html" marginwidth="0" marginheight="0" scrolling="no" width="950" height="630" frameBorder="0"></iframe>

Once the entire maze has been explored the algorithm can then use information it gathered during it's traversal to find the optimal shortest path to solve the maze, shown in red. **By the end of this post you will know how this simple algorithm can perform such a magical and important task.**

layer-by-layer
=======

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

