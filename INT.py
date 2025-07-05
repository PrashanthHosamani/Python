from collections import deque

def water_jug_problem(cap1, cap2, target):
    visited = set() 
    queue = deque([0, 0])
    
    while queue:
        x, y = queue.popleft()
        
        #if target is achived 
        if x == target or y == target:
            return True
        
        if (x, y) in visited:
            continue
        
        queue.extend([
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x)),
        ])
    
    return False

cap1, cap2, target = 4, 3, 2
if water_jug_problem(cap1, cap2, target):
    print(f"It is possible to measure {target} liters.")
else:
    print(f"It is not possible to measure {target} litres.")