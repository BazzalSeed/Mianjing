"""
Summarize
-----------------
-1. bubble sort
0. Insertion sort
1. Insertion Sort
2. heapsort
3. mergesort
4. quicksort
5. Radix Sort https://www.ics.uci.edu/~eppstein/161/960123.html
6. oblivious-merge sort

Categorization
-------------------
comparision
Excpet 5
non-comparison
5

non-ob
6
oblivious
others
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
Merge Sort
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
Randomized Quicksort
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
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def quick_swap(alist, index_a, index_b):
    temp = alist[index_a]
    alist[index_a] = alist[index_b]
    alist[index_b] = temp


def partition(alist, first, last):
    from random import randint
    pivot = randint(first, last)
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