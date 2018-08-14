# Stack ADT
	* A stack ADT is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
	This end is commonly referred to as the “top.” The end opposite the top is known as the “base.” This ordering principle is sometimes called LIFO,
	last-in first-out. It provides an ordering based on length of time in the collection. Newer items are near the top, while older items are near the
	base.
		* Important Observation - The order that elements are removed is OPPOSITE of the order that they are added.
		* It is possible to implement a stack as a python list with the top element as the end of the list
		* It possible to implement a stack as a singly linked list and a pointer to the top element.

	* Operation/method definitions for stack -
		* Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
			* push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
			* pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
			* peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
			* isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
			* size() returns the number of items on the stack. It needs no parameters and returns an integer.