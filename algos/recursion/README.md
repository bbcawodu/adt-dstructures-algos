# Recursion - Recursive Algorithms, Functions, and Procedural Abstractions
  * Recursion definition - the repeated application of a recursive procedure or definition.
  * Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.
  * All recursive algorithms must obey three important laws:
    * A recursive algorithm must have a base case.
      * A base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly. 
    * A recursive algorithm must change its state and move toward the base case.
      * We must arrange for a change of state that moves the algorithm toward the base case. A change of state means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way.
    * A recursive algorithm must call itself, recursively.
      * The algorithm must call itself. This is the very definition of recursion. Recursion is a confusing concept to many beginning programmers. As a novice programmer, you have learned that functions are good because you can take a large problem and break it up into smaller problems. The smaller problems can be solved by writing a function to solve each problem. When we talk about recursion it may seem that we are talking ourselves in circles. We have a problem to solve with a function, but that function solves the problem by calling itself! But the logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into a smaller and easier problems.

# Visualizing Recursion
  * Visualizing recursion is important. These will be notes about vizualizing recursion
  
  # Fractals