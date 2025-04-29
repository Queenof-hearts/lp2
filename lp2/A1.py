# The given Python program implements both Depth First Search (DFS) and Breadth First Search (BFS) 
# traversals on a user-defined graph. In the main() function, the user is prompted to input the number 
# of nodes and, for each node, the number of edges and their connections. The graph is stored as a dictionary
# where each key is a node, and its value is a list of adjacent nodes (neighbors). The DFS traversal is handled
# by the dfs() function, which uses recursion to explore as far as possible along each branch before backtracking.
# It starts from node 1, prints the node, marks it as visited, and then recursively visits each unvisited neighbor. 
# On the other hand, the BFS traversal is managed by the bfs() function, which uses a queue to explore nodes level by level.
# It starts from node 1, adds it to the queue, and then iteratively visits the front of the queue, enqueues all unvisited neighbors,
# and marks them as visited. Both functions ensure that each node is visited only once using a visited set. When executed, the user can 
# simulate graph traversal, and the outputs will show the order of nodes visited in DFS and BFS starting from node 1. This helps in understanding 
# how DFS goes deep into each path, while BFS explores all immediate neighbors first.

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set() # TO keep track of DFS visited nodes
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)

    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)

if __name__=="__main__":
    main()


    # graph = {
    #     '1' : ['2','3'],
    #     '2' : ['4', '5'],
    #     '3' : ['6','7'],
    #     '4' : [],
    #     '5' : [],
    #     '6' : [],
    #     '7' : []
    #     DFS : 1 2 4 5 3 6 7 
    #     BFS : 1 2 3 4 5 6 7 
    # }
