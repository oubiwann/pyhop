# Pyhop, version 1.2.2
## A simple HTN planning system written in Python

----

Copyright 2013 Dana S. Nau - <http://www.cs.umd.edu/~nau>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

----

Pyhop is a simple HTN planner written in Python. 
It works in both Python 2.7 and 3.2. 

Pyhop was easy to implement (less than 150 lines of code), and if you understand the basic ideas of HTN planning ([this presentation](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contains a quick summary),
Pyhop should be easy to understand.

Pyhop's planning algorithm is like the one in [SHOP](http://www.cs.umd.edu/projects/shop/), but with these differences:

  1. States of the world are represented using ordinary variable bindings, not logical propositions. A state is just a Python object that contains the variable bindings.  For example, to say that vehicle <code>v</code> is at location <code>d</code> in state <code>s</code>, you might write <br>
  <code> s.loc['v'] = 'd' </code>
  - HTN operators and methods aren't written in a specialized language. Instead, they're ordinary Python functions. The current state (e.g., <code>s</code> in the above example) is passed to them as an argument.
  - Unlike SHOP, Pyhop doesn't do Horn-clause inference in the preconditions of the HTN methods and operators. It's easier to write the tests directly in Python.




