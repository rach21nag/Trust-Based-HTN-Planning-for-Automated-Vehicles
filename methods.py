import pyhop
import operators


def manual_driving(state, a, x, y):
    if state.trust_level[x][y] < 4:
        return [('human_takeover', a, x, y)]
    return False


def auto_pilot(state, a, x, y):
    if state.trust_level[x][y] >= 4 and state.time[a] >= operators.time_calculation(state.dist[x][y]):
        return [('start_automated_vehicle', a, x), ('call_htn_automated_vehicle', a, x, y), ('estimated_time', a)]
    return False


pyhop.declare_methods('travel', manual_driving, auto_pilot)
print('')
pyhop.print_methods()
