#  Computing the Sum of an Array
	* Suppose you want to calculate the sum of the elements in an array. A standard approach would be to iterate through each element of the array, keep a running total of the sum, and add each element to that sum. A function implementing such an algorithm follows:
	```
	def listsum(numList):
	    theSum = 0
	    for i in numList:
	        theSum = theSum + i
	    return theSum
	```
	* Now suppose that you do not have iterative constructs like a for and while loop. How would you compute the sum of an array? Writing a recursive function is a possible solution. Recall that addition is a function that is defined for 2 parameters, a pair of numbers. If you redfine the problem of computing the sum of an array of numbers as rewriting the array as a fully parenthesized addition expression, the innermost expression is a problem that can be solved without a loop or any iterative constructs. eg: the sum of the array [1,3,5,7,9] can be rewritten as (1+(3+(5+(7+9)))) with the innermost expression as (7+9). This idea can be implemented as a recursive function. These functions are defined in this module.
	* When you show the series of recursive calls that are needed to sum the list [1,3,5,7,9]. You should think of this series of calls as a series of simplifications. Each time we make a recursive call we are solving a smaller problem, until we reach the point where the problem cannot get any smaller. When we reach the point where the problem is as simple as it can get, we begin to piece together the solutions of each of the small problems until the initial problem is solved.