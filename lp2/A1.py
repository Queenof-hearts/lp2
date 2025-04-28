# Taking input from user to create the graph
graph = {}

n = int(input("Enter the number of nodes in the graph: "))
for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# ---------------- DFS ----------------
visited_dfs = set()

def dfs(visited, graph, node, goal_node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        if node == goal_node:
            return True  # Goal found, stop recursion
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal_node):
                return True
    return False

print("\nFollowing is the Path using Depth-First Search:")
dfs(visited_dfs, graph, start_node, goal_node)

# ---------------- BFS ----------------
visited_bfs = []
queue = []

def bfs(visited, graph, node, goal_node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        if s == goal_node:
            break  # Goal found, stop BFS

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("\n\nFollowing is the Path using Breadth-First Search:")
bfs(visited_bfs, graph, start_node, goal_node)
