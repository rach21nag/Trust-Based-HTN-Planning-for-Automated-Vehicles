import pyhop
import operators
import methods

state1 = pyhop.State('state1')
state1.loc = {'me': 'source'}
state1.time = {'me': 60}
state1.time_taken = {'me': 0}
state1.time_left = {'me': 60}
state1.trust_level = {'source': {'destination': 2}, 'destination': {'source': 3}}
state1.dist = {'source': {'destination': 6}, 'destination': {'source': 6}}

print("""
********************************************************************************
Call pyhop.pyhop(state1,[('travel','me','source','destination')]) with different verbosity levels
********************************************************************************
""")

print("- If verbose=0 (the default), Pyhop returns the solution but prints nothing.\n")
pyhop.pyhop(state1, [('travel', 'me', 'source', 'destination')])

print('- If verbose=1, Pyhop prints the problem and solution, and returns the solution:')
pyhop.pyhop(state1, [('travel', 'me', 'source', 'destination')], verbose=1)

print('- If verbose=2, Pyhop also prints a note at each recursive call:')
pyhop.pyhop(state1, [('travel', 'me', 'source', 'destination')], verbose=2)

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1, [('travel', 'me', 'source', 'destination')], verbose=3)
