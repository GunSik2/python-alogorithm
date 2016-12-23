# Bubble Sort
# Time: O(n^2)
# Conceptual Diagram : https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

def bubbleSort(list):
    keepOn = True
    step = 1
    while keepOn:
        keepOn = False
        for index in range(len(list) - 1):
            if list[index] > list[index + 1]:
                # swap two element
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                # need more cycle
                keepOn = True

        print("step " + str(step) + " : " + str(list))
        step += 1
    return list

if __name__ == "__main__":
    list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubbleSort(list))
