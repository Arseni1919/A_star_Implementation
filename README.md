# Simple Implementation Of A* Algorithm

This is **short** and **simple** generic implementation of the [A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm).
You can redefine any part of the code for your own purposes.

## How To Use

### Nodes

Class of Nodes is defined as follows:

```python
class Node:
    def __init__(self, ID, x, y, neighbours):
        self.ID = ID
        self.x = x
        self.y = y
        self.neighbours = neighbours
        self.parent = None
        self.g = 0
        self.h = 0

    def f(self):
        return self.g + self.h
```

Each Node has to have:

- position (x and y)
- unique ID (`int`)
- list of it's neighbours' IDs (list of `int`s)

### Process

Create Nodes.
Put all created Nodes inside a list.
Pick one node as a `start_node` and one node as `goal_node`.
Then insert all of these inside an `a_star` function as follows:

```python
result = a_star(start=node_start, goal=node_goal, nodes=nodes)
```

The `result` will be *None* if there is no solution.
Otherwise, the `result` will contain the list of nodes
representing the path of a solution (from goal to start).



## A* Algorithm

The pseudocode:

![A star](static/a_star_pseudocode.png)

### Example Of Heuristic Function

```python
def heuristic(from_node, to_node):
    return np.sqrt((from_node.x - to_node.x) ** 2 + (from_node.y - to_node.y) ** 2)
```

### Example Of `w` Function

```python
def way(node_current, node_successor):
    return heuristic(node_current, node_successor)
```

## Credits

- [pseudocode](https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf)

