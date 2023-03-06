import pyhop


def go_step(state, step):
    if step == 'refuel':
        return [('refuel',)]
    # print("In go step")
    state.fuel_level = state.fuel_level - 2
    state.nhop = state.nhop + 1
    state.prev_source = (state.loc["x"], state.loc["y"])
    # print(state.prev_source)
    if step == 'east':
        return [('go_east',)]
    elif step == 'west':
        return [('go_west',)]
    elif step == 'north':
        return [('go_north',)]
    elif step == 'south':
        return [('go_south',)]

    return False


def move(state, dx, dy):
    # print("In Move")
    state.visited[state.loc['x']][state.loc['y']] = True

    print("im in move")
    if state.fuel_level < 4:
        return [('go_step', 'refuel'), ('travel', dx, dy)]
    if state.loc['y'] < dy:
        return [('go_step', 'east'), ('travel', dx, dy)]
    elif state.loc['y'] > dy:
        return [('go_step', 'west'), ('travel', dx, dy)]

    if state.loc['x'] < dx:
        return [('go_step', 'south'), ('travel', dx, dy)]
    elif state.loc['x'] > dx:
        return [('go_step', 'north'), ('travel', dx, dy)]

    return False


def pedestrian_scene(state, dx, dy):
    if state.loc['x'] == dx and state.loc['y'] == dy:
        return [('finish',)]

    pa_count, light = state.maze[state.loc['x']][state.loc['y']]

    if pa_count > 0:
        if pa_count < state.pa_threshold:
            return [('stop',), ('move', dx, dy)]
        else:
            return [('alt_route', dx, dy), ('finish',)]

    return False


def night_scenario(state, dx, dy):
    if state.loc['x'] == dx and state.loc['y'] == dy:
        return [('finish',)]

    pa_count, light = state.maze[state.loc['x']][state.loc['y']]
    print(pa_count, light)

    if light < 700:
        if pa_count == 0:
            return [('move', dx, dy)]

        if pa_count > 0:
            if light > 200:
                return [('stop',), ('move', dx, dy)]
            elif state.light_threshold < light < 200:
                return [('light_on',), ('stop',), ('move', dx, dy)]
            elif light < state.light_threshold:
                return [('alt_route', dx, dy), ('finish',)]

    return False


pyhop.declare_methods('go_step', go_step)
pyhop.declare_methods('move', move)
pyhop.declare_methods('travel', night_scenario, pedestrian_scene, move)


