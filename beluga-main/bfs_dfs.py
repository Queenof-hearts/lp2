graph={}
n=int(input("enter number of nodes: "))
for i in range (n):
    node = input(f"enter node {i+1} name: ")
    neighbors = input (f"enter the neighbors of {i+1} separated by spaces: ").split()
    graph[node]=neighbors

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s=queue.pop(0)
        print(s,end=' ')
        for neighbors in graph[s]:
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors)

visited_dfs=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)

start_node=input("enter starting node for BFS and DFS: ")
print("\nBFS traversal: ")
bfs(visited,graph,start_node)

print("\nDFS traversal: ")
dfs(visited_dfs,graph,start_node)

