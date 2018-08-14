# Queue ADT
	* A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.
	* The most recently added item in the queue must wait at the end of the collection. The item that has been in the collection the longest is at the front. This ordering principle is sometimes called FIFO, first-in first-out. It is also known as “first-come first-served.”
		* Important Observation - The order that elements are removed is SAME as the order that they are added.
	* Operation/method definitions for stack -
		* Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
			* enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
			* dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
			* isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
			* size() returns the number of items in the queue. It needs no parameters and returns an integer.