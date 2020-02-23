
# a graph is basically a list of nodes
class Graph:
    def __init__(self):
        self.nodes = []

# each node has a list of children nodes, and a name
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        # true means that the node has been visited
        self.visited = False

import collections

# this method finds whether two nodes have a route
# Time: O(N) - the number of vertices in the graph | Space: O(N)
def search(start, end):
    if start == end:
        return True

    # bfs - queue - can also be used to find the shortest path
    queue = collections.deque([start])
    start.visited = True
    while len(queue):
        node = queue.popleft()

        if node is not None:
            for connectedNode in node.children:
                if not connectedNode.visited:
                    if connectedNode == end:
                        return True
                    queue.append(connectedNode)
        
        node.visted = True
    
    return False

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

nodeA.children = [nodeB, nodeC, nodeD]
nodeB.children = [nodeD]
nodeD.children = [nodeF]

print(search(nodeB, nodeF))











