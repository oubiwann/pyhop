"""
Pyhop, version 2.0 -- a simple SHOP-like planner written in Python.
Author: Dana S. Nau, 2013.05.31

Copyright 2013 Dana S. Nau - http://www.cs.umd.edu/~nau

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Pyhop should work correctly in both Python 2.7 and Python 3.2.
For examples of how to use it, see the example files that come with Pyhop.

Pyhop provides the following classes and functions:

- foo = State('foo') tells Pyhop to create an empty state object named 'foo'.
  To put variables and values into it, you should do assignments such as
  foo.var1 = val1

- bar = Goal('bar') tells Pyhop to create an empty goal object named 'bar'.
  To put variables and values into it, you should do assignments such as
  bar.var1 = val1

- helpers.print_state(foo) will print the variables and values in the state foo.

- helpers.print_goal(foo) will print the variables and values in the goal foo.

- declare_operators(o1, o2, ..., ok) tells Pyhop that o1, o2, ..., ok
  are all of the planning operators; this supersedes any previous call
  to declare_operators.

- print_operators() will print out the list of available operators.

- declare_methods('foo', m1, m2, ..., mk) tells Pyhop that m1, m2, ..., mk
  are all of the methods for tasks having 'foo' as their taskname; this
  supersedes any previous call to declare_methods('foo', ...).

- helpers.print_methods() will print out a list of all declared methods.

- plan(state1,tasklist) tells Pyhop to find a plan for accomplishing tasklist
  (a list of tasks), starting from an initial state state1, using whatever
  methods and operators you declared previously.

- In the above call to plan, you can add an optional 3rd argument called
  'verbose' that tells plan how much debugging printout it should provide:
- if verbose = 0 (the default), plan returns the solution but prints nothing;
- if verbose = 1, it prints the initial parameters and the answer;
- if verbose = 2, it also prints a message on each recursive call;
- if verbose = 3, it also prints info about what it's computing.
"""

# Pyhop's planning algorithm is very similar to the one in SHOP and JSHOP
# (see http://www.cs.umd.edu/projects/shop). Like SHOP and JSHOP, Pyhop uses
# HTN methods to decompose tasks into smaller and smaller subtasks, until it
# finds tasks that correspond directly to actions. But Pyhop differs from
# SHOP and JSHOP in several ways that should make it easier to use Pyhop
# as part of other programs:
#
# (1) In Pyhop, one writes methods and operators as ordinary Python functions
#     (rather than using a special-purpose language, as in SHOP and JSHOP).
#
# (2) Instead of representing states as collections of logical assertions,
#     Pyhop uses state-variable representation: a state is a Python object
#     that contains variable bindings. For example, to define a state in
#     which box b is located in room r1, you might write something like this:
#     s = State()
#     s.loc['b'] = 'r1'
#
# (3) You also can define goals as Python objects. For example, to specify
#     that a goal of having box b in room r2, you might write this:
#     g = Goal()
#     g.loc['b'] = 'r2'
#     Like most HTN planners, Pyhop will ignore g unless you explicitly
#     tell it what to do with g. You can do that by referring to g in
#     your methods and operators, and passing g to them as an argument.
#     In the same fashion, you could tell Pyhop to achieve any one of
#     several different goals, or to achieve them in some desired sequence.
#
# (4) Unlike SHOP and JSHOP, Pyhop doesn't include a Horn-clause inference
#     engine for evaluating preconditions of operators and methods. So far,
#     I've seen no need for it; I've found it easier to write precondition
#     evaluations directly in Python. But I could consider adding such a
#     feature if someone convinces me that it's really necessary.
#
# Accompanying this file are several files that give examples of how to use
# Pyhop. To run them, launch python and type "import blocks_world_examples"
# or "import simple_travel_example".
from __future__ import print_function
import copy

# from pyhop.helpers import (
#     helpers.print_goal, print_methods, helpers.print_operators, helpers.print_state)
from . import helpers


############################################################
# States and goals

class State:
    """A state is just a collection of variable bindings."""
    def __init__(self,name):
        self.__name__ = name

class Goal:
    """A goal is just a collection of variable bindings."""
    def __init__(self,name):
        self.__name__ = name

############################################################
# Commands to tell Pyhop what the operators and methods are

operators = {}
methods = {}

def declare_operators(*op_list):
    """
    Call this after defining the operators, to tell Pyhop what they are.
    op_list must be a list of functions, not strings.
    """
    operators.update({op.__name__:op for op in op_list})
    return operators

def declare_methods(task_name,*method_list):
    """
    Call this once for each task, to tell Pyhop what the methods are.
    task_name must be a string.
    method_list must be a list of functions, not strings.
    """
    methods.update({task_name:list(method_list)})
    return methods[task_name]

def get_operators():
    return operators

def get_methods():
    return methods

############################################################
# The actual planner

def plan(state,tasks,operators,methods,verbose=0):
    """
    Try to find a plan that accomplishes tasks in state.
    If successful, return the plan. Otherwise return False.
    """
    if verbose>0: print(
        '** hop, verbose={}: **\n   state = {}\n   tasks = {}'.format(
            verbose, state.__name__, tasks))
    result = seek_plan(state,tasks,operators,methods,[],0,verbose)
    if verbose>0: print('** result =',result,'\n')
    return result

def search_operators(state,tasks,operators,methods,plan,task,depth,verbose):
    if verbose>2:
        print('depth {} action {}'.format(depth,task))
    operator = operators[task[0]]
    newstate = operator(copy.deepcopy(state),*task[1:])
    if verbose>2:
        print('depth {} new state:'.format(depth))
        helpers.print_state(newstate)
    if newstate:
        solution = seek_plan(
            newstate,tasks[1:],operators,methods,plan+[task],depth+1,verbose)
        if solution != False:
            return solution

def search_methods(state,tasks,operators,methods,plan,task,depth,verbose):
    if verbose>2:
        print('depth {} method instance {}'.format(depth,task))
    relevant = methods[task[0]]
    for method in relevant:
        subtasks = method(state,*task[1:])
        # Can't just say "if subtasks:", because that's wrong if
        # subtasks == []
        if verbose>2:
            print('depth {} new tasks: {}'.format(depth,subtasks))
        if subtasks != False:
            solution = seek_plan(
                state,subtasks+tasks[1:],operators,methods,plan,depth+1,verbose)
            if solution != False:
                return solution

def seek_plan(state,tasks,operators,methods,plan,depth,verbose=0):
    """
    Workhorse for pyhop. state, tasks, operators, and methods are as in the
    plam function.
    - plan is the current partial plan.
    - depth is the recursion depth, for use in debugging
    - verbose is whether to print debugging messages
    """
    if verbose>1:
        print('depth {} tasks {}'.format(depth,tasks))
    if tasks == []:
        if verbose>2:
            print('depth {} returns plan {}'.format(depth,plan))
        return plan
    task = tasks[0]
    if task[0] in operators:
        return search_operators(
            state,tasks,operators,methods,plan,task,depth,verbose)
    if task[0] in methods:
        return search_methods(
            state,tasks,operators,methods,plan,task,depth,verbose)
    if verbose>2:
        print('depth {} returns failure'.format(depth))
    return False
