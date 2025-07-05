import heapq

def best_first_search(graph, start, goal, heuristic):
    
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    parent = {start: None}
    
    while pq:
        current = heapq.heappop(pq)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(pq (heuristic[neighbor], neighbor))
                
    return None

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'F'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

heuristic = {
    'A' : 6,
    'B' : 4,
    'C' : 5,
    'D' : 2,
    'E' : 1,
    'F' : 0
}

start_node = 'A'
goal_node = 'F'
path = best_first_search(graph, start_node, goal_node, heuristic)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}. ")
    
    
