import random   # The random library contains function to generate a series of random numbers
import time     # The time library contains function to record time taken to implement each algorithm

size_list = [20, 100, 1000, 4000]       # Static list where each number represents size of the array to be generated.
listofvalues = []                       # Used to store and retrieve list of random numbers


# This function generates a series of 'n' random numbers and store to a specified filepath
# The argument 'size' is equivalent to n
def generate_date(size):

    # Initialization of list that will store random numbers
    arr = []

    # creation of string 'filepath' that stores location of output file.
    filename = '/Users/madhavdatt/CSE5311/Project1/' + 'arr' + str(size)

    # Iteratively generate random numbers and append to list
    for i in range(size):
        arr.append(random.randint(0, 6000))

    # The fileobject 'textfile' creates the file where the numbers will be stored
    textfile = open('{0}.txt'.format(filename), "w")

    # Iteratively write the list contents to the file
    for number in arr:
        if number == arr[size-1]:
            textfile.write(str(number))
        else:
            textfile.write(str(number) + ",")

    textfile.close()


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


# Logic for Insertion sort as specified in CLRS. To sort the list, do the following:
# 1: Iterate from A[1] to A[n] and compare current number i.e. key with value on previous index.
# 2: If the key is smaller, compare it with the numbers with 'previous-1', 'previous-2' value and so on.
# 3. Move up greater number by one index to make space for the swapped number.
def insertion_sort():
    for j in range(1, len(listofvalues)):
        key = listofvalues[j]
        i = j - 1
        while i >= 0 and listofvalues[i] > key:
            listofvalues[i + 1] = listofvalues[i]
            i = i - 1
        listofvalues[i + 1] = key


# Below loop performs the following tasks in an iterative manner:
# a). Generate 'n' random numbers where n is an element of 'size_ list' and store into file.
# b). Read numbers from file and store into a list.
# c). Print contents of original array.
# d). Run insertion sort function and create sorted array.
# e). Print sorted array along with time taken to run it.
# f). Clear list for next file to be read and avoiding overwriting
for x in size_list:
    generate_date(x)
    read_file(x)
    print("Original array is {0}".format(listofvalues))
    start = time.time()
    insertion_sort()
    end = time.time()
    print("Sorted array is {0}".format(listofvalues))
    print("Time taken was {0:.5f} seconds".format(end-start))
    print()
    listofvalues.clear()
