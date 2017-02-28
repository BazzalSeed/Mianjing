"""
Summarize
-----------------
-1. bubble sort
0. Insertion sort
1. Insertion Sort
2. heapsort
3. mergesort
4. quicksort
5. Bucket Sort
6. counting sort
7. Radix Sort https://www.ics.uci.edu/~eppstein/161/960123.html
8. oblivious-merge sort
9. bitonic sort

Categorization
-------------------
comparision
==============
others
non-comparison
================
5,6,7

ob
================
8,9
non - oblivious
================
others

Stable
=============
0,1,3

unstable
=============
others




extra
-------------------
Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort?
If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input numbers.
The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware caches more effectively. Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.
"""

"""
-1. bubble sort
"""


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

"""
0. Selection Sort
"""


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


"""
1. Insertion Sort

"""


def insertionsort(alist):
    for i in xrange(1, len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and currentvalue < alist[position - 1]:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue


"""
2.Heap sort
+++++++++++++++++


Heap
___________
A heap can be classified further as either a "max heap" or a "min heap".
In a max heap, the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node.
In a min heap, the keys of parent nodes are less than or equal to those of the children and the lowest key is in the root node.
The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact priority queues are often referred to as "heaps", regardless of how they may be implemented.
A common implementation of a heap is the binary heap,though fibonacci heap is more efficient

heapsort
______________

High-level
================
0. build heap
1. delete max till empty

Complexity:
============================

 Time :Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).
 Space: O(1)

 Approach
=========================
 Heap sort happens in two phases. In the first phase, the array
 is transformed into a heap. A (max)heap is a binary tree where
 1) each node is greater than each of its children
 2) complete tree

 In phase two the heap is continuously reduced to a sorted array:
 1) while the heap is not empty
 - remove the top of the head into an array
 - fix the heap.
 Heap sort was invented by John Williams not by B. R. Heap.

Details
 ======================
 A heap is based on an array just as a hashmap is based on an
 array. For a heap, the children of an element n are at index
 2n+1 for the left child and 2n+2 for the right child.

 The movedown function checks that an element is greater than its
 children. If not the values of element and child are swapped. The
 function continues to check and swap until the element is at a
 position where it is greater than its children.
=======================================================================
"""


def heapsort(alist):
    last_index = len(alist) - 1
    for i in xrange(last_index / 2, -1, -1):
        shiftdown(alist, i, last_index)

    for i in xrange(last_index, 0, -1):
        swap(alist, 0, i)
        shiftdown(alist, 0, i - 1)


def shiftdown(alist, first, last):
    largest = 2 * first + 1

    while largest <= last:
        if largest < last and alist[largest + 1] > alist[largest]:
            largest += 1
        if alist[largest] > alist[first]:
            swap(alist, first, largest)
            first = largest
            largest = 2 * first + 1
        else:
            return


def swap(alist, a, b):
    temp = alist[a]
    alist[a] = alist[b]
    alist[b] = temp

"""
=============================================================================================
"""


"""
3. Merge Sort
"""

"""
Not in-place
"""


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) / 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)


"""
4. Randomized Quicksort
++++++++++++++++++++
High-level
______________
Divide and Conquer
0. randomly pick a pivot
1. Partition and return the split
2. Sort left of the split
3. sort right of the split
Complexity
_______________
Time: Average (O(NlgN)), Best Lg(N), worst (N^2)
Space: O(1)
"""


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first <= last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def quick_swap(alist, index_a, index_b):
    temp = alist[index_a]
    alist[index_a] = alist[index_b]
    alist[index_b] = temp


def partition(alist, first, last):
    from random import randint
    pivot = randint(first, last + 1)
    quick_swap(alist, first, pivot)

    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            quick_swap(alist, leftmark, rightmark)
    quick_swap(alist, first, rightmark)

    return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

"""
5. Bucket Sort
assuming input ditribute normally [0,1]
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket floor([n*array[i]])
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
"""


def insertionsort(alist):
    for i in xrange(1, len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and currentvalue < alist[position - 1]:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue


def bucketsort(alist):
    n = len(alist)
    buckets = [[] for _ in range(n)]
    for i in xrange(len(alist)):
        buckets[int(n * alist[i])].append(alist[i])
    for b in buckets:
        insertionsort(b)

    i = 0
    for b in buckets:
        for j in b:
            alist[i] = j
            i += 1

"""
6. counting sort
+++++++++++++++++++
perfect for sorting chars

Complexity
Time -- O(k+n)
Space -- O(n+k)
==============

"""


def countingsort(alist):
    k = max(alist) + 1
    n = len(alist)
    output = [0 for _ in xrange(n)]
    c = [0 for _ in xrange(k)]
    for j in alist:
        c[j] = c[j] + 1
    for i in xrange(1, k):
        c[i] = c[i] + c[i - 1]
    for i in xrange(n):
        output[c[alist[i]] - 1] = alist[i]
        c[alist[i]] -= 1
    for i in xrange(n):
        alist[i] = output[i]

"""
7. Radix Sort
+++++++++++++++++
What if K = n ^ 2 for couting sort
Use counting sort as subroutine to sort each digit

Time Complexity O(n)
Space O(n)
"""


def radix_countingsort(alist, exp):
    n = len(alist)
    c = [0] * 10
    output = [0] * n
    for j in alist:
        v = j / exp
        c[v % 10] += 1
    for i in range(1, 10):
        c[i] = c[i - 1] + c[i]
    for i in range(n - 1, -1, -1):
        v = alist[i] / exp
        output[c[v % 10] - 1] = alist[i]
        c[v % 10] -= 1
    for i in range(n):
        alist[i] = output[i]


def radixsort(alist):
    exp = 1
    k = max(alist)
    while k != 0:
        radix_countingsort(alist, exp)
        k = k / 10
        exp = exp * 10

"""
Both oblivious sorting use divide and conquer
"""
"""
8. Batcher's odd-even merge sort
++++++++++++++++++++++++++++++++
The idea behind Batcher’s algorithm is the following claim (which at first glance looks incredible):
Divide
    If you sort the first half of a list, and sort the second half separately,
combine
    and then sort theodd-indexed entries (first, third, fifth, ...)
    and the even-indexed entries (second, fourth, sixth, ...)separately
    then you need make only one more comparison-switch per pair of keys to completely sort the list.

IT builds a sorting network
O(n log2n)



• Sort(x1, . . . , xn) calls:
    Sort(x1, . . . , xn/2), then Sort(xn/2+1, . . . , xn), and then Merge(x1, . . . , xn).
• Merge(x1, . . . , xn) calls:
Merge(xi, for i odd), then Merge(xi for i even), and then Comp(x2, x3), Comp(x4, x5), · · ·
Comp(xn−2, xn−1).
• Comp(xi, xj ) means:
compare the key in the position i with the one in position j and put the larger one in position
j, the smaller one in position i.
"""




"""
9. Bitonic Sorting
++++++++++++++++

• Input: Random set of 2n=2k
(k is some positive integer)
numbers. Note that every pair of elements is bitonic.
• Bitonic sequences of size 2 are merged to create ordered lists of
size 2. At the end of this first stage of merging, we actually
have n/4 bitonic sequences of size 4.

• Bitonic sequences of size 4 are merged into sorted sequences of
size 4, alternately into increasing and decreasing order, so as to
form n/8 bitonic sequences of size 8 and so on.

• Given an unordered sequence of size 2n, exactly log2 2n stages
of merging are required to produce a completely ordered list.

• Output : Ordered list of size 2n

• Θ(log2 n) levels of comparators are required to sort completely
an initially unordered list of size 2n when done in parallel.
"""
def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.


def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt / 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

# This funcion first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order


def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt / 2
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

# Caller of bitonicSort for sorting the entire array of length N
# in ASCENDING order


def sort(a, N, up):
    bitonicSort(a, 0, N, up)

# Driver code to test above
a = [3, 7, 4, 8, 6, 2, 1, 5]
n = len(a)
up = 1

sort(a, n, up)
print ("\n\nSorted array is")
for i in range(n):
    print("%d" % a[i]),
