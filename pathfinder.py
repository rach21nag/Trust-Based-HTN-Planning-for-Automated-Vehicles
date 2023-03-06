# # Test Maze
# maze = [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 0, 1]
# ]
# N = len(maze)
#
# # Start point and destination
# source = (2, 2)  # top left corner
# destination = (0, 0)  # bottom right corner


# Check if cell (x, y) is valid or not
def is_valid_cell(x, y, N):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    return True


def find_paths_util(maze, source, destination, visited, path, paths):
    """Find paths using Breadth First Search algorith """
    # Done if destination is found
    if source == destination:
        paths.append(path[:])  # append copy of current path
        return

    # mark current cell as visited
    N = len(maze)
    x, y = source
    visited[x][y] = True


    # if current cell is a valid and open cell,
    if is_valid_cell(x, y, N) and maze[x][y] == 1:
        # Using Breadth First Search on path extension in all direction

        # go right (x, y) --> (x + 1, y)
        if x + 1 < N and (not visited[x + 1][y]):
            path.append((x + 1, y))
            find_paths_util(maze, (x + 1, y), destination, visited, path, paths)
            path.pop()

        # go left (x, y) --> (x - 1, y)
        if x - 1 >= 0 and (not visited[x - 1][y]):
            path.append((x - 1, y))
            find_paths_util(maze, (x - 1, y), destination, visited, path, paths)
            path.pop()

        # go up (x, y) --> (x, y + 1)
        if y + 1 < N and (not visited[x][y + 1]):
            path.append((x, y + 1))
            find_paths_util(maze, (x, y + 1), destination, visited, path, paths)
            path.pop()

        # go down (x, y) --> (x, y - 1)
        if y - 1 >= 0 and (not visited[x][y - 1]):
            path.append((x, y - 1))
            find_paths_util(maze, (x, y - 1), destination, visited, path, paths)
            path.pop()

        # Unmark current cell as visited
    visited[x][y] = False

    return paths


def find_paths(maze, visited, source, destination):
    """ Sets up and searches for paths"""
    N = len(maze)  # size of Maze is N x N

    # 2D matrix to keep track of cells involved in current path
    # visited = [[False]*N for _ in range(N)]
    print(maze)
    path = [source]
    paths = []
    paths = find_paths_util(maze, source, destination, visited, path, paths)

    return paths

#
# # Find all paths
# paths = find_paths(maze, source, destination)
#
# print("Paths with '->' separator between maze cell locations")
# for path in paths:
#   print(*path, sep = ' -> ')
