# Merge Sort
  * Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item,
  it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively
  invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge,
  is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
  * The mergeSort function shown in begins by asking the base case question. 
    * If the length of the list is less than or equal to one, then we already have a sorted list and no more processing is necessary.
    * If, on the other hand, the length is greater than one, then we use the Python slice operation to extract the left and right halves.
    * It is important to note that the list may not have an even number of items. That does not matter, as the lengths
    will differ by at most one.
  * Once the mergeSort function is invoked on the left half and the right half (lines 8–9), it is assumed they are sorted.
  The helper function (line 16) is responsible for merging the two smaller sorted lists into a larger sorted list.
    * Notice that the merge operation places the items back into the original list (baseist) one at a time by repeatedly
    taking the smallest item from the sorted lists. Note that the statement lefthalf[i] <= righthalf[j] ensures that
    the algorithm is stable. A stable algorithm maintains the order of duplicate items in a list and is preferred in most cases.
  * Merge sort is an 𝑂(𝑛log𝑛) algorithm.
  * It is important to notice that the mergeSort function requires extra space to hold the two halves as they are extracted
  with the slicing operations. This additional space can be a critical factor if the list is large and can make this
  sort problematic when working on large data sets.