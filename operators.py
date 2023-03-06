import pyhop


def time_calculation(dist):
    return 2 * dist


def human_takeover(state, a, x, y):
    if state.loc[a] == x:
        state.loc[a] = y
        return state
    else:
        return False


def start_automated_vehicle(state, a, x):
    state.loc['autopilot'] = x
    return state


def call_htn_automated_vehicle(state, a, x, y):
    if state.loc['autopilot'] == x and state.loc[a] == x:
        state.loc['autopilot'] = y
        state.loc[a] = y
        state.time_taken[a] = time_calculation(state.dist[x][y])
        return state
    else:
        return False


def estimated_time(state, a):
    if state.time[a] >= state.time_taken[a]:
        state.time_left[a] = state.time[a] - state.time_taken[a]
        return state
    else:
        return False


pyhop.declare_operators(human_takeover, start_automated_vehicle, call_htn_automated_vehicle, estimated_time)
print('')
pyhop.print_operators()
