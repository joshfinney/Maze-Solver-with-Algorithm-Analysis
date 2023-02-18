import os

def read_maze(file_name):
    # read the maze from a text file and return it as a 2D list
    with open(file_name, 'r') as file:
        maze = [list(line.strip()) for line in file]
    height = len(maze)
    width = len(maze[0])
    return maze, height, width

def print_maze(maze):
    # print the maze
    for row in maze:
        print(''.join(row))

def dfs(maze, visited, x, y):
    # perform depth-first search
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        # out of bounds
        return False
    if visited[y][x] or maze[y][x] == '#':
        # already visited or wall
        return False
    if y == len(maze) - 1:
        # reached the goal
        return True
    visited[y][x] = True
    # explore the adjacent nodes
    if dfs(maze, visited, x-1, y): # left
        print(f"({y}, {x})")
        return True
    if dfs(maze, visited, x+1, y): # right
        print(f"({y}, {x})")
        return True
    if dfs(maze, visited, x, y-1): # up
        print(f"({y}, {x})")
        return True
    if dfs(maze, visited, x, y+1): # down
        print(f"({y}, {x})")
        return True
    return False

def solve_maze(file_name):
    maze, height, width = read_maze(file_name)
    print_maze(maze)
    # check the size of the maze
    if height < 2 or width < 2:
        print("Error: invalid maze size.")
        return

    # find the starting position
    start_x = maze[0].index('-')
    start_y = 0

    if start_x < 0:
        print("Error: Starting position not found.")
        return

    # initialize the visited matrix
    visited = [[False for _ in range(width)] for _ in range(height)]

    # solve the maze using depth-first search
    dfs(maze, visited, start_x, start_y)

def main():
    os.chdir(r"/Users/josh/Documents/GitHub/artificial-intelligence-ca-2023/")
    solve_maze('maze-files/maze-Small.txt')


if __name__ == "__main__":
    main()