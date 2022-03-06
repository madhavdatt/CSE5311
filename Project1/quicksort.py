import time     # The time library contains function to record time taken to implement each algorithm

size_list = [20, 100, 1000, 4000]       # Static list where each number represents size of the array to be generated.
listofvalues = []                       # Used to store and retrieve list of random numbers.


# This function reads from a file and stores the numbers in a list.
def read_file(size):

    # Read from file using readline() function. This generates a string.
    # Split the string when you encounter a separator (comma in our case).
    fileobj = open('/Users/madhavdatt/CSE5311/Project1/arr{0}.txt'.format(size), 'r')
    field = (fileobj.readline()).split(',')

    # Iterate through the list of strings.
    # When a string is encountered, check to see if it is a number using isdigit() function.
    # If yes, convert into 'int' datatype and append to list
    for num in field:
        if num.isdigit():
            listofvalues.append(int(num))
    fileobj.close()


# We have implemented quick sort from the pseudocode inherited from CLRS.
# It begins at the leftmost element, and uses i to keep track of the index of smaller (or equal to) elements.
# While traversing, if a smaller element is found, we swap current element with arr[i]. Else, we ignore current element.
def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


# In QuickSort, we pick an element as pivot and partition the array around the pivot.
# Any element in the array can be chosen as pivot. Here, we have picked the last element as pivot.
# All other elements (excluding the pivot) are divided into two partitions.
# First partition contains elements smaller than the pivot, and second partition contains elements greater than it.
# After sorting both partitions recursively,  we join the first sorted partition, pivot, and second sorted partition.
def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q + 1, r)


# Below loop performs the following tasks in an iterative manner:
# a). Read numbers from file and store into a list.
# b). Print contents of original array.
# c). Run quick sort function and create sorted array.
# d). Print sorted array along with time taken to run it.
# e). Clear lists for next file to be read and avoiding overwriting
for val in size_list:
    read_file(val)
    print("Original array is {0}".format(listofvalues))
    start = time.time()
    quick_sort(listofvalues, 0, len(listofvalues)-1)
    end = time.time()
    print("Sorted array is {0}".format(listofvalues))
    print("Time taken was {0:.5f} seconds".format(end-start))
    print()
    listofvalues.clear()
