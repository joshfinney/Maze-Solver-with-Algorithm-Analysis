def read_maze(file_name):
    with open(file_name, 'r') as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze

def dfs(maze):
    stack = [(0, i) for i in range(len(maze[0])) if maze[0][i] == '-']  # Initialize stack with start node
    visited = set(stack)  # Mark start node as visited
    path_dict = {(0, i): [(0, i)] for i in range(len(maze[0])) if maze[0][i] == '-'}  # Initialize path dict with start node

    while stack:
        node = stack.pop()
        if node[0] == len(maze) - 1:  # Check if goal is reached
            return path_dict[node]

        for neighbor in get_neighbors(node, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                path_dict[neighbor] = path_dict[node] + [neighbor]

    return "Maze is unsolvable"

def get_neighbors(node, maze):
    row, col = node
    neighbors = []

    if row > 0 and maze[row-1][col] == '-':  # Check North neighbor
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == '-':  # Check South neighbor
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] == '-':  # Check West neighbor
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == '-':  # Check East neighbor
        neighbors.append((row, col+1))

    return neighbors

def main():
    maze = read_maze('maze-Small.txt')
    path = dfs(maze)

    if path != "Maze is unsolvable":
        print("The path from the start to the goal is:")
        for node in path:
            print(node)
    else:
        print("The maze is unsolvable.")


if __name__ == "__main__":
    main()