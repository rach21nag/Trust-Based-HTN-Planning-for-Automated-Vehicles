import pyhop
import pathfinder


def refuel(state):
    state.fuel_level = 10
    return state


# def battery(dist):
#     return 1.5 * dist
#
#
# def time_used(dist):
#     return 2 * dist


def go_north(state):
    # print("In North")
    # state.nhop = state.nhop + 1
    if state.loc['x'] > 0:
        state.loc['x'] = state.loc['x'] - 1
    return state


def go_east(state):
    # print("In East")
    # state.nhop = state.nhop + 1
    if state.loc['y'] < 4:
        state.loc['y'] = state.loc['y'] + 1
        return state
    return False


def go_south(state):
    # print("In South")
    # state.nhop = state.nhop + 1
    if state.loc['x'] < 4:
        state.loc['x'] = state.loc['x'] + 1
    return state


def go_west(state):
    # print("In West")
    # state.nhop = state.nhop + 1
    if state.loc['y'] > 0:
        state.loc['y'] = state.loc['y'] - 1
    return state


def stop(state):
    return state


def finish(state):
    return state


def make_alt_path_maze(state):
    maze = state.maze
    rows = len(maze)
    cols = len(maze[0])

    maze_t = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            p, l = maze[i][j]

            if p < state.pa_threshold and l > state.light_threshold:
                maze_t[i][j] = 1
    return maze_t


def alt_route(state, dx, dy):
    source = state.prev_source
    destination = (dx, dy)

    maze = make_alt_path_maze(state)
    # maze[state.loc["x"]][state.loc["y"]] = 1

    paths = pathfinder.find_paths(maze, state.visited, source, destination)
    for path in paths:
        hops = len(path) - 1
        print(*path, sep=' -> ')
        print("hops:", hops)
    return state


def light_on(state):
    state.light = state.light + 100
    return state


pyhop.declare_operators(go_east, go_west, go_north, go_south, stop, alt_route, finish, light_on, refuel)
