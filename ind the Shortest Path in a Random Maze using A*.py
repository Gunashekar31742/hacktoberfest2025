import heapq
import random

ROWS, COLS = 15, 30
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_maze(rows, cols):
    maze = [[random.choice([' ', '#']) for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 'S'
    maze[rows - 1][cols - 1] = 'G'
    return maze

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for dr, dc in DIRS:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
    return None

def display_maze(maze, path=None):
    maze_copy = [row[:] for row in maze]
    if path:
        for r, c in path:
            if maze_copy[r][c] not in ('S', 'G'):
                maze_copy[r][c] = '.'
    for row in maze_copy:
        print(''.join(row))
    print()

maze = generate_maze(ROWS, COLS)
start = (0, 0)
goal = (ROWS - 1, COLS - 1)
print("Generated Maze:")
display_maze(maze)
path = a_star(maze, start, goal)
if path:
    print("Path found! ✅")
    display_maze(maze, path)
else:
    print("No path found ❌")
