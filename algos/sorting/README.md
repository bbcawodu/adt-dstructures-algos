# Sorting - Sorting Algorithms, Functions, and Procedural Abstractions
  * Sorting is the process of placing elements from a collection in some kind of order. For example, a list of words
  could be sorted alphabetically or by length.
  * There are many sorting algorithms that have been developed and analyzed. This suggests that sorting is an important
  area of study in computer science. Sorting a large number of items can take a substantial amount of computing resources.
  Like searching, the efficiency of a sorting algorithm is related to the number of items being processed. For small
  collections, a complex sorting method may be more trouble than it is worth. The overhead may be too high. On the other
  hand, for larger collections, we want to take advantage of as many improvements as possible.
  * Before getting into specific algorithms, we should think about the operations that can be used to analyze a sorting process.
    * First, it will be necessary to compare two values to see which is smaller (or larger). In order to sort a collection,
    it will be necessary to have some systematic way to compare values to see if they are out of order. The total number
    of comparisons will be the most common way to measure a sort procedure.
    * Second, when values are not in the correct position with respect to one another, it may be necessary to exchange
    them. This exchange is a costly operation and the total number of exchanges will also be important for evaluating
    the overall efficiency of the algorithm.