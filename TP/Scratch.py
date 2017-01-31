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


def mergesort(alist):
    if len(alist)>1:
        start, end = 0, len(alist) -1
        mid = start + (start-end)/2

        left = alist[:mid]
        right = alist[mid:]
        mergesort(left)
        mergesort(right)


        left_i, right_i, i = 0,0,0
        left_last, right_last = len(left) , len(right)

        while  (left_i < left_last) and (right_i < right_last):
            if left[left_i] < right[right_i]:
                alist[i] = left[left_i]
                left_i += 1
            else:
                alist[i] = right[right_i]
                right_i += 1
            i += 1
        while left_i < left_last:
            alist[i] = left[left_i]
            left_i += 1
            i += 1
        while right_i < right_last:
            alist[i] = right[right_i]
            right_i += 1
            i += 1
