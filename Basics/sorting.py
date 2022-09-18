

test1 = [5, 6, 2, 20, 10, 19, 3, 35, 1, 500]
test2 = [5, 6, 2, 20, 10, 19, 3, 35, 1, 500]
test3 = [5, 6, 2, 20, 10, 19, 3, 35, 1, 500]
test4 = [5, 6, 2, 20, 10, 19, 3, 35, 1, 500]
test5 = [5, 6, 2, 20, 10, 19, 3, 35, 1, 500]




def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while((j >= 0) & (arr[j] > key)):
            arr[j+1] = test1[j]
            j = j - 1
        arr[j+1] = key;

    for a in arr:
        print(a)


def Selection_sort(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    for a in arr:
        print(a)


def Bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    for a in arr:
        print(a)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)






#Insertion_sort(test1)
#Selection_sort(test2)
#Bubble_sort(test3)
n = len(test4)
mergeSort(test4, 0, n-1)
for i in range(len(test4)):
    print(test4[i])
