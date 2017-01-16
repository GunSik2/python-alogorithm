#40m
def insertionSort(list):
    for currentPointer in range(1, len(list)):
        currentValue = list[currentPointer]
        pointer = currentPointer - 1;
        while currentValue < list[pointer] and pointer >= 0:
            list[pointer + 1] = list[pointer]
            pointer = pointer - 1
        list[pointer + 1] = currentValue
        print(str(currentPointer) + " : " + str(list))
    return list

if __name__ == "__main__":
    list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insertionSort(list))
