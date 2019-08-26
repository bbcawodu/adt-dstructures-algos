# Sequential Search
  * When data items are stored in a collection such as a python list, we say that they have a linear or sequential
  relationship. Each data item is stored in a position relative to the others. In Python lists, these relative positions
  are the index values of the individual items.
  * Since these index values are ordered, it is possible for us to visit them in sequence. This process gives rise to
  our first searching technique, the sequential search.
  
  # Sequential Search algorithm
   * Starting at the first item in the list, we simply move from item to item, following the underlying sequential
   ordering until we either find what we are looking for or run out of items. If we run out of items, we have
   discovered that the item we were searching for was not present.
   # Analysis of Sequential Search
   * Unordered List
                      Best Case Worst Case Average Case
     item is present     1            𝑛          𝑛/2
     item is not present 𝑛            𝑛           𝑛
    * Ordered List
     item is present     1            𝑛          𝑛/2
     item is not present 1            𝑛           𝑛