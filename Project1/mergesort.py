import sys      # This library allows us to specify the sentinel value by using 'sys.maxsize' constant
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


# Here, we combine the sorted sub-arrays into a larger sorted array.
# To hold the left and right sub-arrays, temporary arrays 'L' & 'R' are created.
# This is done by increasing size of the sub-arrays by 1 and placing a sentinel value(sys.maxsize) in the last position.
# This avoids indexing outside either sub-array when merging the arrays back together.
# When we reach sentinel value in one sub-array, remaining non-sentinel values in other subarray will be less than it.
# The two sentinels are not compared because the original array is smaller than the total lengths of the sub-arrays.
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [None] * (n1+1)
    R = [None] * (n2+1)

    for i in range(n1):
        L[i] = arr[p + i]

    for j in range(n2):
        R[j] = arr[q + j + 1]

    L[n1] = sys.maxsize
    R[n2] = sys.maxsize

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


# We use the recursive function 'merge_sort', supplying first and last item index to this function.
# First, we check if the portion of the array we're looking at has at least two elements.
# The array is already sorted if there is only one element.
# Then we calculate the array's middle index, used to create left (a[min-mid]) and right (a[mid+1, a[max]) sub-arrays.
# Finally, we use the function 'Merge' to combine the two sorted sub-arrays into a single sorted array.
# Both merge_sort() and merge() are based on the pseudocode described in CLRS
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


# Below loop performs the following tasks in an iterative manner:
# a). Read numbers from file and store into a list.
# b). Print contents of original array.
# c). Run merge sort function and create sorted array.
# d). Print sorted array along with time taken to run it.
# e). Clear lists for next file to be read and avoiding overwriting
for x in size_list:
    read_file(x)
    print("Original array is {0}".format(listofvalues))
    start = time.time()
    merge_sort(listofvalues, 0, len(listofvalues)-1)
    end = time.time()
    print("Sorted array is {0}".format(listofvalues))
    print("Time taken was {0:.5f} seconds".format(end-start))
    print()
    listofvalues.clear()
