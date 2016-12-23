# BinarySearch
# Conceptal Diagram: https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm

def binarySearch(item, list):
    found = False
    top = len(list) - 1
    bottom = 0

    while not found and bottom < top:
        middle = (top - bottom) // 2 + bottom
        print("step = " + str(bottom) + " < " + str(middle)  + " < " + str(top))

        if item == list[middle]:
            found = True
        elif item < list[middle]:
            top = middle
        else:
            bottom = middle
    return found


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    item = int(input("Which number do you want to find?" ))
    isitFound = binarySearch(item, list)
    if isitFound == True:
        print("The number " + str(item) + " was found in the list")
    else:
        print("The number " + str(item) + " wasn't found in the list")
