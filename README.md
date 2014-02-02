# PyHOP, version 2.0

A Hierarchical Ordered Planner for Python

## Introduction

PyHOP is a simple hierarchical task network (HTN) planner written in Python. It works in both Python 2.7 and 3.2.

PyHOP was easy to implement (less than 150 lines of code), and if you understand the basic ideas of HTN planning ([this presentation](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contains a quick summary),
PyHOP should be easy to understand.

PyHOP's planning algorithm is like the one in [SHOP](http://www.cs.umd.edu/projects/shop/), but with several differences that should make it easier to integrate it with ordinary computer programs:

  - PyHOP represents states of the world using ordinary variable bindings, not logical propositions. A state is just a Python object that contains the variable bindings.  For example, you might write s.loc['v'] = 'd' to say that vehicle v is at location d in state s.

  - To write HTN operators and methods for PyHOP, you don't need to learn a specialized planning language. Instead, you write them as ordinary Python functions. The current state (e.g., s in the above example) is passed to them as an argument.

## Installation

```bash
$ git clone https://github.com/oubiwann/pyhop.git
$ cd pyhop
$ sudo python setup.py install
```

## Examples

The code comes with several examples. These can be run in the following manner:

```bash
$ git clone https://github.com/oubiwann/pyhop.git
$ cd pyhop
$ python examples/simple_travel.py
$ python examples/blocks_world/run1.py
$ python examples/blocks_world/run2.py
```


## Changes from Version 1

With versison 2.0, the following change were made:
* code has now been converted to a Python package, complete with ``setup.py`` file
* slight changes to the API have been made (the planner function ``pyhop`` has been ranamed to ``plan``)
* slight changes to some of the helper functions have been made (added another parameter to help generalize)
* examples have been moved into their own directory

## License
----

Copyright 2013 Dana S. Nau - <http://www.cs.umd.edu/~nau>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

----
