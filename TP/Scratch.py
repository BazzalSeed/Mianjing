# def quicksort(alist):
#     quicksorthelper(alist, 0, len(alist) - 1)
#
#
# def quicksorthelper(alist, start, end):
#     if start < end:
#         split = parition(alist, start, end)
#         quicksorthelper(alist,start, split - 1)
#         quicksorthelper(alist, split + 1, end)
#
#
# def parition(alist, start, end):
#     from random import randint
#     pivot = randint(start, end)
#     swap(alist, start, pivot)
#
#     pivotvalue = alist[start]
#     done = False
#     leftmark = start + 1
#     rightmark = end
#     while not done:
#         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#             leftmark += 1
#         while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
#             rightmark -= 1
#         if leftmark > rightmark:
#             done = True
#         else:
#             swap(alist, leftmark, rightmark)
#     swap(alist, start, rightmark)
#     return rightmark
#
#
# def swap(alist, a, b):
#     temp = alist[a]
#     alist[a] = alist[b]
#     alist[b] = temp
#
# def heapsort(alist):
#     last_index = len(alist) - 1
#     for i in xrange(last_index/2, -1, -1):
#         shiftdown(alist, i, last_index)
#
#     for i in xrange(last_index, 0, -1):
#         swap(alist, 0, i)
#         shiftdown(alist,0,i-1)
#
# def shiftdown(alist, first, last):
#     largest = 2*first + 1
#
#     while largest <= last:
#         if largest < last and alist[largest+1] > alist[largest]:
#             largest += 1
#         if alist[largest] > alist[first]:
#             swap(alist, first, largest)
#             first = largest
#             largest = 2*first + 1
#         else:
#             return
#
#
# def swap(alist, a, b):
#     temp = alist[a]
#     alist[a] = alist[b]
#     alist[b] = temp

#
# def mergesort(alist):
#     if len(alist) > 1:
#         start, end = 0, len(alist) - 1
#         mid = start + (start - end) / 2
#
#         left = alist[:mid]
#         right = alist[mid:]
#         mergesort(left)
#         mergesort(right)
#
#         left_i, right_i, i = 0, 0, 0
#         left_last, right_last = len(left), len(right)
#
#         while (left_i < left_last) and (right_i < right_last):
#             if left[left_i] < right[right_i]:
#                 alist[i] = left[left_i]
#                 left_i += 1
#             else:
#                 alist[i] = right[right_i]
#                 right_i += 1
#             i += 1
#         while left_i < left_last:
#             alist[i] = left[left_i]
#             left_i += 1
#             i += 1
#         while right_i < right_last:
#             alist[i] = right[right_i]
#             right_i += 1
#             i += 1


def quickselect(alist, k):
    start, end = 0, len(alist) - 1
    return quickselecthelper(alist, start, end, k)


def quickselecthelper(alist, start, end, k):
    if start <= end:
        split = random_partition(alist, start, end)
        print start + k, split, start, end
        if k == split:
            print "found"
            return alist[start + k]
        elif k < split:
            return quickselecthelper(alist, start, split - 1, k)
        else:
            return quickselecthelper(alist, split + 1, end, k)


def random_partition(alist, start, end):
    from random import randint
    pivot = randint(start, end)
    temp = alist[start]
    alist[start] = alist[pivot]
    alist[pivot] = temp

    leftmark = start + 1
    rightmark = end
    done = False
    pivotvalue = alist[start]

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            swap(alist, leftmark, rightmark)

    swap(alist, start, rightmark)
    return rightmark


def swap(alist, a, b):
    temp = alist[a]
    alist[a] = alist[b]
    alist[b] = temp


def random_partition(alist, start, end):
    from random import randint
    pivot = randint(start, end)
    swap(alist, start, pivot)

    leftmark = start + 1
    rightmark = end
    done = False
    pivotvalue = alist[start]

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            swap(alist, leftmark, rightmark)

    swap(alist, start, rightmark)
    return rightmark


def partition(alist, start, end, x):
    # find the index of the pivot
    pivot = 0
    for j in range(start, end):
        if alist[j] == x:
            pivot = j
            break
    swap(alist, start, pivot)

    leftmark = start + 1
    rightmark = end
    done = False
    pivotvalue = alist[start]

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            swap(alist, leftmark, rightmark)

    swap(alist, start, rightmark)
    return rightmark


def swap(alist, a, b):
    temp = alist[a]
    alist[a] = alist[b]
    alist[b] = temp


def select(alist, i):
    return selecthelper(alist, 0, len(alist) - 1, i)
# find the ith biggest element in A[p:r]


def selecthelper(alist, start, end, i):

    # divide the n elements of A into n / 5 groups
    groups = [[]] * (((end + 1 - start) + 4) / 5)
    for x in range(start, end + 1):
        # print (x-start)/5, x, len(groups)
        # print groups[(x-start)/5]
        # print alist,len(alist),alist[x]
        groups[(x - start) / 5] += [alist[x]]
        # print "done"
    # find the median of each group
    medians = [sorted(l)[(len(l) - 1) / 2] for l in groups]

    # find the median of medians
    if len(medians) == 1:
        median_to_rule_them_all = medians[0]
    else:
        median_to_rule_them_all = selecthelper(medians, 0, len(medians) - 1, (len(medians) - 1) / 2)

    # partition A around the median of medians
    partition_index = partition(alist, start, end, median_to_rule_them_all)

    if i == partition_index:
        return alist[i]
    elif i < partition_index:
        return selecthelper(alist, start, partition_index - 1, i)
    else:
        return selecthelper(alist, partition_index + 1, end, i)


# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
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
