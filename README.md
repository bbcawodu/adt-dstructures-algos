# Abstract Data Types, Data Structures, and Algorithms
  * This repo serves as an overview of abstract data types, data structures, and algorithms.
  * Large Portions of this repo uses [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/runestone/static/pythonds/index.html) as a reference.

  
## Computer Science Fundamentals Overview
  * Computer science is the study of problems, the problem solving process(Algorithms), and solutions that come from the process.
    * Algorithms describe the solution to a problem in terms of the data needed to represent the problem instance and the set of
    steps necessary to produce the intended result

  * Computer science uses abstraction as a tool for representing both processes and data.
  * Procedural abstraction (Eg. Functions)
    * We simply describe the interface: the name of the function, what is needed (the parameters), and what will be returned. The details are hidden
    inside.
  * Data abstraction (Eg. Classes and built-in data types)
    * Abstract Data Type - a logical description of how we view the data from the perspective of the user, including the operations that are allowed 
    without regard to how they will be implemented
    * Data Structure - a physical view of the data from the perspective of the implementer using some collection of programming constructs and primitive data types.
    They can be used to implement Abstract Data Types
    * To put it simply, ADT is a logical description and data structure is concrete. ADT is the logical picture of the data and the operations
    to manipulate the component elements of the data. A data structure is a concrete implementation of the specification provided by an ADT. ADT
    is in the logical level and data structure is in the implementation level.
      * NOTE: example: linked list is a Data Structure, and every data structure is more specigic/implemented version of an ADT, so linked list is both.
  * Abstract data types allow programmers to manage the complexity of a problem domain by hiding the details of the data.

  * Programming is the process of taking an algorithm and encoding it into a notation, a programming language, so that it can be executed by a
  computer.
  * Programming languages must provide a notational way to represent both the process and the data. To this end, languages provide control
  constructs and data types.
    * Control constructs allow algorithmic steps to be represented in a convenient yet unambiguous way. At a minimum, algorithms require
    constructs that perform sequential processing, selection for decision-making, and iteration for repetitive control. As long as the language
    provides these basic statements, it can be used for algorithm representation.
    * All data items in the computer are represented as strings of binary digits. In order to give these strings meaning, we need to have data
    types. Data types provide an interpretation for this binary data so that we can think about the data in terms that make sense with respect
    to the problem being solved. These low-level, built-in data types (sometimes called the primitive data types) provide the building blocks
    for algorithm development.

  * Python
    * Python is a powerful, yet easy-to-use, object-oriented language.
    * Lists, tuples, and strings are built in Python sequential collections.
    * Dictionaries and sets are nonsequential collections of data.
    * Classes allow programmers to implement data structures.
    * Programmers can override standard methods as well as create new methods.
    * Classes can be organized into hierarchies.
    * A class constructor(__init__) should always invoke the constructor of its parent before continuing on with its own data and behavior.
  * Javasctipt
    * Javascript is a powerful interpreted(program where each line is executed freely without the whole program being compiled) language designed to be run in browser
      * Javascript runtimes(program designed to perform the execution model) do exist. (NodeJS)
    * Prototype based language
      * Each object has a prototype object that it inherits attributes and methods from.
      * Form a prototype chain in which powerful abstract data type/data structure heiarchies can be created
      * An object's prototype is not to be confused with constructor/prototype functions.
        * The prototype of an object is descrbed above, while constructor/prototype functions act as ways to describe/implement new objects(data structures).
  * Javascript's Promise vs Python's Deferred
    * Promises and Deferreds are similar in that they both represent ways to encode the execution order of asynchronous(interleaved) code while being decoupled from synchronous(one after the other) code.
    * The difference is that Promises represent the eventual completion(resolve) or failure(reject) of an asynchronous operation, returning/awating it's resulting value(s). While Deferreds represent the encoding of the execution order of asynchronous code while also returning/yielding the results of completion to callback functions(callbacks) or errors to error functions(errbacks). A subtle distinction.

## Algorithmic Analysis Overview
  * Algorithm analysis is an implementation-independent way of measuring an algorithm.
  * Algorithms can be analyzed based on their space or time requirements. There is often a trade off between space and time when
  optimizing an algorithm.
    * Big-O notation allows algorithms to be classified by their dominant process with respect to the size of the problem.
      * e.g. T(n)=1+n
        * The parameter n is often referred to as the “size of the problem,” and we can read this as “T(n) is the time it takes to solve a problem
        of size n, namely 1+n steps.”
      * The above T(n) has an order of magnitude function of O(n)
        * The order of magnitude function describes the part of T(n) that increases the fastest as the value of n increases. Order of magnitude is
        often called Big-O notation (for “order”) and written as O(f(n)). It provides a useful approximation to the actual number of steps in the
        computation. The function f(n) inside the O() provides a simple representation of the dominant part of the original T(n).
      * A list of common order of magnitude functions in increasing order of time taken
        * f(n)  Name
        * 1     Constant
        * logn  Logarithmic
        * n     Linear
        * nlogn Log Linear
        * n^2   Quadratic
        * n^3   Cubic
        * 2^n   Exponential
        * n!    Factorial

## Problem Solving Approach Guidlines
  * ALWAYS RESTATE PROBLEM OUT LOUD IN YOUR OWN WORDS
  * ALWAYS GET EXAMPLES FOR THE PROBLEM(CONCRETE/SPECIFIC SAMPLE/EXAMPLE INPUTS AND OUTPUTS FOR THE PROBLEM).
  * ALWAYS CHECK ASSUMPTIONS ABOUT THE PROBLEM
  * ALWAYS WORK THROUGH A SAMPLE SOLUTION IN YOUR MIND/OUT LOUD/ON THE BOARD(WITHOUT CODE) BEFORE ATTEMPTING TO CODE SOLUTION.
    - ALWAYS WALK THROUGH SAMPLE/EXAMPLE INPUTS AND OUTPUTS PLUGGED INTO SAMPLE SOLUTION.
    - ALWAYS CHECK TIME AND SPACE COMPLEXITIES OF THE SAMPLE SOLUTION
  * ALWAYS ENCODE THE SAMPLE SOLUTION INTO AN ACTUAL PROGRAMMING LANGUAGE AND NOT PSEUDO CODE.
    * ALWAYS WALK THROUGH SAMPLE/EXAMPLE INPUTS AND OUTPUTS PLUGGED INTO CODED SAMPLE SOLUTION.

## ADTs, Data Structures, and Algorithms Explained and Implemented
  * [ADTs and Data Structures](adts-dstructures/README.md)
  * [Algorithms](algos/README.md)

## Acknowledgements
  * [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/runestone/static/pythonds/index.html)
