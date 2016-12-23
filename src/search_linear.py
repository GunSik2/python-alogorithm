# Linear Search
# Conputal Diagram: https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm

def linearSearch(item, list):
    found = False
    position = 0
    while position < len(list) and not found:
        if list[position] == item:
            found = True
        position += 1
    return found


if __name__ == "__main__":
    shopping = ["apple", "banana", "pasta"]
    item = input("Which item do you want to find?")
    isitFound = linearSearch(item, shopping)
    if isitFound:
        print("Your item is in the list")
    else:
        print("Your item is not in the list")