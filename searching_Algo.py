
# LINEAR SEARCH ALGORITHM
# Searches for an element by comparing the key element with all other elements in the list
# 1. Create a function that will accept the data list, the length of list and key element
# 2. If an element matches the key element, return the curresponding index number
# 3. If the element is not found, return -1

def linearSearch(myArray, n, key):
    for x in range(0, n):
        if (myArray[x] == key):
            return x
    return -1

myArray = [34, 1, 8, 19, 0, 12]
key = 19
n = len(myArray)
matched = linearSearch(myArray, n, key)
if (matched == -1):
    print(f'{key} is not present in the list')
else:
    print(f'{key} is present at index {matched}.')


# BINARY SEARCH ALGORITHM
# Used to search for a element in a sorted array by making use of the Decrease-and-Conquer algorithm
# Compare the key with the middle element and then dividing the array into half if it doesn't match the middle element
# The left half is searched if the element is smaller than the middle element using the same binary search method
# The right half is searched if the element is larger than the middle element using the same binary search method

def binarySearch(myList, key):
    left = 0
    right = len(myList) - 1
    matched = False

    while(left <= right and not matched):
        middle = (left + right) // 2
        if myList[middle] == key:
            matched = True
        else:
            if key < myList[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return matched

print(binarySearch([2, 3, 56, 13, 1], 56))
print(binarySearch([2, 3, 56, 13, 1], 26))
