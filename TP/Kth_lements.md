# Find kth element

## Method 1(Use Sorting)

- Sort the elements in descending order in O(nLogn)
- Print the first k numbers of the sorted array O(k).
- Time complexity: O(nlogn)

### Method 2 (Use Bubble k times)

- Modify Bubble Sort to run the outer loop at most k times.
- Print the last k elements of the array obtained in step 1.
- Time Complexity: O(nk)

Like Bubble sort, other sorting algorithms like Selection Sort can also be modified to get the k largest elements.

### Method 3(Use Max Heap)

- Build a Max Heap tree in O(n)
- Use Extract Max k times to get k maximum elements from the Max Heap O(klogn)
- Time complexity: O(n + klogn)

### Method 4(Quick Select)

In order to find the k-th order statistics in a region of size n
* use the randomized partition to split the region into two subarrays.
* Let s − 1 and n − s be the size of the left subarray and the size of the right subarray.
    * If k = s, the pivot is the key that's looked for.
    * If k ≤ s − 1, look for the k-th element in the left subarray.
    * Otherwise, look for the (k − s)-th one in the right subarray
* Time Complexity: Expected Time O(n)

```

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
```
Method 5(Worst Case Linear Time)
Select
* Divide the input n items into n/5 [n/5] sets -- O(N)
* find the median of each [n/5] sets -- O(N)
* Takes these[n/5] medians and put them in another array [medians_of_medians],  use select to recursively find the median of this new array=> get median_of_median -- T(n/5)
* partition the original array using median_of_median get split
* then
    * if start + split == k : return alist[start+split]
    * elif start + split < k : recurse on right
    * else recurse on left
-- T(max(median_of_median_index-start, end - median_of_median_index ))

```
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

```
