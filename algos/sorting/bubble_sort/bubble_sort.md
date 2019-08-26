# Bubble Sort
  * Bubble sort makes multiple passes through a list. It compares adjacent items and exchanges or swaps those that are out of order.
  Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the
  location where it belongs.
  * After completing 𝑛−1 passes, the smallest item must be in the correct position with no further processing required.
  * The exchange operation, sometimes called a “swap,” is slightly different in Python than in most other programming languages.
  Typically, swapping two elements in a list requires a temporary storage location (an additional memory location). In Python,
  it is possible to perform simultaneous assignment. The statement a,b=b,a will result in two assignment statements being
  done at the same time. Using simultaneous assignment, the exchange operation can be done in one statement.
  * To analyze the bubble sort, we should note that regardless of how the items are arranged in the initial list, 𝑛−1
  passes will be made to sort a list of size n. The table below shows the number of comparisons for each pass.
  The total number of comparisons is the sum of the first 𝑛−1 integers. Recall that the sum of the first n integers is
  (1/2)𝑛^2 + (1/2)𝑛. The sum of the first 𝑛−1 integers is (1/2)𝑛^2 + (1/2)𝑛 - n, which is (1/2)𝑛^2 - (1/2)𝑛. This is
  still 𝑂(𝑛2) comparisons. In the best case, if the list is already ordered, no exchanges will be made. However, in
  the worst case, every comparison will cause an exchange. On average, we exchange half of the time.
    * Pass    Comparisons 
     
      1         n−1
     
      2         n−2
     
      3         n−3
     
      …          …
     
      n−1       1
  * A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final
  location is known. These “wasted” exchange operations are very costly. However, because the bubble sort makes passes
  through the entire unsorted portion of the list, it has the capability to do something most sorting algorithms cannot.
  In particular, if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can
  be modified to stop early if it finds that the list has become sorted. This means that for lists that require just a few
  passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop.
  