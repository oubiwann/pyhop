"""
Blocks-world test data for Pyhop 1.1.
Author: Dana Nau <nau@cs.umd.edu>, November 15, 2012
This file should work correctly in both Python 2.7 and Python 3.2.
"""
from __future__ import print_function
from pyhop import hop, helpers

import operators
import methods1


print('')
helpers.print_operators(hop.get_operators())
print('')
helpers.print_methods(hop.get_methods())

#############     beginning of tests     ################

print("""
****************************************
First, test pyhop on some of the operators and smaller tasks
****************************************
""")

print("- Define state1: a on b, b on tale, c on table")

"""
A state is a collection of all of the state variables and their values. Every
state variable in the domain should have a value.
"""

state1 = hop.State('state1')
state1.pos={'a':'b', 'b':'table', 'c':'table'}
state1.clear={'c':True, 'b':False,'a':True}
state1.holding=False

helpers.print_state(state1)
print('')

print('- these should fail:')
hop.plan(state1,[('pickup','a')], hop.get_operators(), hop.get_methods(), verbose=1)
hop.plan(state1,[('pickup','b')], hop.get_operators(), hop.get_methods(), verbose=1)
print('- these should succeed:')
hop.plan(state1,[('pickup','c')], hop.get_operators(), hop.get_methods(), verbose=1)
hop.plan(state1,[('unstack','a','b')], hop.get_operators(), hop.get_methods(), verbose=1)
hop.plan(state1,[('get','a')], hop.get_operators(), hop.get_methods(), verbose=1)
print('- this should fail:')
hop.plan(state1,[('get','b')], hop.get_operators(), hop.get_methods(), verbose=1)
print('- this should succeed:')
hop.plan(state1,[('get','c')], hop.get_operators(), hop.get_methods(), verbose=1)

print("""
****************************************
Run pyhop on two block-stacking problems, both of which start in state1.
The goal for the 2nd problem omits some of the conditions in the goal
of the 1st problemk, but those conditions will need to be achieved
anyway, so both goals should produce the same plan.
****************************************
""")

print("- Define goal1a:")

"""
A goal is a collection of some (but not necessarily all) of the state variables
and their desired values. Below, both goal1a and goal1b specify c on b, and b
on a. The difference is that goal1a also specifies that a is on table and the
hand is empty.
"""

goal1a = hop.Goal('goal1a')
goal1a.pos={'c':'b', 'b':'a', 'a':'table'}
goal1a.clear={'c':True, 'b':False, 'a':False}
goal1a.holding=False

helpers.print_goal(goal1a)
print('')

print("- Define goal1b:")

goal1b = hop.Goal('goal1b')
goal1b.pos={'c':'b', 'b':'a'}

helpers.print_goal(goal1b)

### goal1b omits some of the conditions of goal1a,
### but those conditions will need to be achieved anyway


hop.plan(state1,[('move_blocks', goal1a)], hop.get_operators(), hop.get_methods(), verbose=1)
hop.plan(state1,[('move_blocks', goal1b)], hop.get_operators(), hop.get_methods(), verbose=1)

print("""
****************************************
Run pyhop on two more planning problems. As before, the 2nd goal omits
some of the conditions in the 1st goal, but both goals should produce
the same plan.
****************************************
""")

print("- Define state 2:")

state2 = hop.State('state2')
state2.pos={'a':'c', 'b':'d', 'c':'table', 'd':'table'}
state2.clear={'a':True, 'c':False,'b':True, 'd':False}
state2.holding=False

helpers.print_state(state2)
print('')

print("- Define goal2a:")

goal2a = hop.Goal('goal2a')
goal2a.pos={'b':'c', 'a':'d', 'c':'table', 'd':'table'}
goal2a.clear={'a':True, 'c':False,'b':True, 'd':False}
goal2a.holding=False

helpers.print_goal(goal2a)
print('')

print("- Define goal2b:")

goal2b = hop.Goal('goal2b')
goal2b.pos={'b':'c', 'a':'d'}

helpers.print_goal(goal2b)
print('')


### goal2b omits some of the conditions of goal2a,
### but those conditions will need to be achieved anyway.

hop.plan(state2,[('move_blocks', goal2a)], hop.get_operators(), hop.get_methods(), verbose=1)
hop.plan(state2,[('move_blocks', goal2b)], hop.get_operators(), hop.get_methods(), verbose=1)


print("""
****************************************
Test pyhop on planning problem bw_large_d from the SHOP distribution.
****************************************
""")

print("- Define state3:")

state3 = hop.State('state3')
state3.pos = {1:12, 12:13, 13:'table', 11:10, 10:5, 5:4, 4:14, 14:15,
              15:'table', 9:8, 8:7, 7:6, 6:'table', 19:18, 18:17, 17:16,
              16:3, 3:2, 2:'table'}
state3.clear = {x:False for x in range(1,20)}
state3.clear.update({1:True, 11:True, 9:True, 19:True})
state3.holding = False

helpers.print_state(state3)
print('')

print("- Define goal3:")

goal3 = hop.Goal('goal3')
goal3.pos = {15:13, 13:8, 8:9, 9:4, 4:'table', 12:2, 2:3, 3:16, 16:11, 11:7,
             7:6, 6:'table'}
goal3.clear = {17:True, 15:True, 12:True}

helpers.print_goal(goal3)
print('')

hop.plan(state3,[('move_blocks', goal3)], hop.get_operators(), hop.get_methods(), verbose=1)
