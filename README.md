# Pyhop, version 1.2.2
## A simple SHOP-like planning system written in Python

----

Copyright 2013 Dana S. Nau - <http://www.cs.umd.edu/~nau>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

----

### Pyhop source code

pyhop.py contains the Pyhop source code, which should work correctly in both Python 2.7 and Python 3.2.
It provides the following classes and functions:

- foo = State('foo') tells Pyhop to create an empty state object named 'foo'. To put variables and values into it, you should do assignments such as foo.var1 = val1

- bar = Goal('bar') tells Pyhop to create an empty goal object named 'bar'. To put variables and values into it, you should do assignments such as bar.var1 = val1

- print_state(foo) will print the variables and values in the state foo.

- print_goal(foo) will print the variables and values in the goal foo.

- declare_operators(o1, o2, ..., ok) tells Pyhop that o1, o2, ..., ok are all of the planning operators; this supersedes any previous call to declare_operators.

- print_operators() will print out the list of available operators.

- declare_methods('foo', m1, m2, ..., mk) tells Pyhop that m1, m2, ..., mk are all of the methods for tasks having 'foo' as their taskname; this supersedes any previous call to declare_methods('foo', ...).

- print_methods() will print out a list of all declared methods.

- pyhop(state1,tasklist) tells Pyhop to find a plan for accomplishing tasklist (a list of tasks), starting from an initial state state1, using whatever methods and operators you declared previously.

- In the above call to pyhop, you can add an optional 3rd argument called
  'verbose' that tells pyhop how much debugging printout it should provide:
    - if verbose = 0 (the default), pyhop returns the solution but prints nothing;
    - if verbose = 1, it prints the initial parameters and the answer;
    - if verbose = 2, it also prints a message on each recursive call;
    - if verbose = 3, it also prints info about what it's computing.

### Examples

Also included are two examples of how to use Pyhop. To run them, you should launch Python and import the following two files: 

- simple_travel_example.py - a very simple example involving travel from one location to another.

- blocks_world_examples.py - a more complicated example that implements the block-stacking algorithm in <http://www.cs.umd.edu/~nau/papers/gupta1992complexity.pdf>

----

This file is in Markdown format.
