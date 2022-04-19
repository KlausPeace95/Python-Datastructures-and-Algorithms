
# MERGE SORT
# Follows Divide-and-Conquer rule
# Divides the list into smaller list until each list consists of just one element (sorted)
# Then compares adjacent list and rearrange them in the desired order recursively until only one sorted list remains
def mergeSort(myList, left, right):
    if right - left > 1: # Checks whether there are at least two elements in the list
        middle = (left + right) // 2
        mergeSort(myList, left, middle)
        mergeSort(myList, middle, right)
        mergeList(myList, left, middle, right)

def mergeList(myList, left, middle, right):
    leftList = myList[left:middle]
    rightList = myList[middle:right]
    k = left
    i = 0
    j = 0

    while(left + i < middle and middle + j < right):
        if (leftList[i] <= rightList[j]):
            myList[k] = leftList[i]
            i = i + 1
        else:
            myList[k] = rightList[j]
            j = j + 1
        k = k + 1
    if left + i < middle:
        while k < right:
            myList[k] = leftList[i]
            i = i + 1
            k = k + 1
    else:
        while k < right:
            myList[k] = rightList[j]
            j = j + 1
            k = k + 1


# Prompting User to input values to sort

myList = input('Enter the list to be sorted using merge sort: ').split()
myList = [int(x) for x in myList]
mergeSort(myList, 0, len(myList))
print('The Sorted List is: ')
print(myList)


# BUBBLE SORT
# Compares and sort adjacent elements if they are not in the desired or specified order
def bubbleSort(a):
    b = len(a) -1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1] = a[y+1],a[y]
    return a
a=[45,67,8,1,7,0]
bubbleSort(a)
print(a)

# INSERTION SORT
# Picks one element at a time and place it at the exact position where it belongs to
def insertionSort(a):
    for x in range(1, len(a)):
        k = a[x]
        j = x - 1
        while j >= 0 and k < a[j]:  # Sort in Ascending order (Change k < a[j] to k > a[j] for descending order)
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k

a = [90, -23, 0, 4, 21, 33]
insertionSort(a)
print(a)


# SELECTION SORT
# Splits the list into two halves, first half is the sorted list and second half is the unsorted list
# Initially, sorted list is empty and all elements are in unsorted list
# Looks in the unsorted list,picks up the item that is supposed to come first and place in the sorted list and repeats this step

def selectionSort(myArray, r):
    for x in range(r):
        minimum = x
        for y in range(x + 1, r):
            if myArray[y] < myArray[minimum]:
                minimum = y
        (myArray[x], myArray[minimum]) = (myArray[minimum], myArray[x])

myList = [47, 90, 12, -34, 0, 77, 9]
r = len(myList)
selectionSort(myList, r)
print(myList)

# SHELL SORT
# Sort the elements apart from each order
def shellSort(myArray, n):
    gap = n // 1     # Dividing number of elements by two to find gap
    while gap > 0:
        for x in range(gap, n):
            y = myArray[x]
            z = x
            while z >= gap and myArray[z - gap] > y:
                myArray[z] = myArray[z - gap]
                z -= gap
            myArray[z] = y
        gap //= 2
myList = [23, 12, 1, 17, 45, 2, 13]
length = len(myList)
shellSort(myList, length)
print(myList)
