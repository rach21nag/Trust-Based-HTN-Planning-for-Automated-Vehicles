import pyhop
import pathfinder

import methods
import operators

state1 = pyhop.State('state1')
state1.loc = {'x': 2, 'y': 0}
state1.pa_threshold = 15
state1.light = 0
state1.pa_count = 0
state1.nhop = 0
state1.fuel_used = 0
state1.fuel_level = 100
state1.light_threshold = 100
state1.prev_source = (0, 0)
state1.maze = [
    [(0, 1000), (0, 1000), (0, 1000), (0, 1000), (0, 1000)],
    [(0, 1000), (0, 135), (1, 1000), (3, 1000), (0, 150)],
    [(0, 1500), (1, 1050), (12, 1000), (3, 1000), (0, 1000)],
    [(3, 1000), (2, 5000), (1, 1000), (20, 1220), (0, 1000)],
    [(1, 1000), (6, 1000), (9, 110), (1, 1500), (0, 1000)]
]

state1.visited = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
]

print("""
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Call
pyhop.pyhop(state1, [('travel', 0, 0)])
with different verbosity levels
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
""")

print("- If verbose=0 (the default), Pyhop returns the solution but prints nothing.\n")
pyhop.pyhop(state1, [('travel', 4, 3)])

print('- If verbose=1, Pyhop prints the problem and solution, and returns the solution:')
pyhop.pyhop(state1, [('travel', 4, 3)], verbose=1)

print('- If verbose=2, Pyhop also prints a note at each recursive call:')
pyhop.pyhop(state1, [('travel', 4, 3)], verbose=2)

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1, [('travel', 4, 3)], verbose=3)
