# Binary Search
  * It is possible to take advantage of an ordered list if we are clever with our search comparisons.
  * In the sequential search, when we compare against the first item, there are at most 𝑛−1 more items to look through
  if the first item is not what we are looking for. Instead of searching the list in sequence, a binary search will
  start by examining the middle item. 
    * If that item is the one we are searching for, we are done. 
    * If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
      * If the item we are searching for is greater than the middle item, we know that the entire lower half of the
      list as well as the middle item can be eliminated from further consideration. The item, if it is in the list,
      must be in the upper half.
  * This algorithm is a great example of a divide and conquer strategy. Divide and conquer means that we divide the
  problem into smaller pieces, solve the smaller pieces in some way, and then reassemble the whole problem to get the result.
  * When we perform a binary search of a list, we first check the middle item. If the item we are searching for is less
  than the middle item, we can simply perform a binary search of the left half of the original list. Likewise,
  if the item is greater, we can perform a binary search of the right half. Either way, this is a recursive call to
  the binary search function passing a smaller list.
  * The time complexity of binary search is O(logn)
  * Even though a binary search is generally better than a sequential search, it is important to note that for small
  values of n, the additional cost of sorting is probably not worth it. In fact, we should always consider whether it
  is cost effective to take on the extra work of sorting to gain searching benefits. If we can sort once and then
  search many times, the cost of the sort is not so significant. However, for large lists, sorting even once can be so
  expensive that simply performing a sequential search from the start may be the best choice.