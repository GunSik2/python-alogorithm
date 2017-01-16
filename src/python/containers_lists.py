## Lists
print("## Lists")
xs = [3, 1, 2]      # Create a list
print(xs, xs[2])   # print(s "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; print(s "2"
xs[2] = 'foo'    # Lists can contain elements of different types
print(xs)         # print(s "[3, 1, 'foo']"
xs.append('bar') # Add a new element to the end of the list
print(xs)         # print(s "[3, 1, 'foo', 'bar']"
x = xs.pop()     # Remove and return the last element of the list
print(x, xs)      # print(s "bar [3, 1, 'foo']"


## Slicing
print("## Slicing")
nums = list(range(5))    # range is a built-in function that creates a list of integers
print(type(nums))
print(nums)         # print(s "[0, 1, 2, 3, 4]"
print(nums[2:4])    # Get a slice from index 2 to 4 (exclusive); print(s "[2, 3]"
print(nums[2:])     # Get a slice from index 2 to the end; print(s "[2, 3, 4]"
print(nums[:2])     # Get a slice from the start to index 2 (exclusive); print(s "[0, 1]"
print(nums[:])      # Get a slice of the whole list; print(s ["0, 1, 2, 3, 4]"
print(nums[:-1])    # Slice indices can be negative; print(s ["0, 1, 2, 3]"
nums[2:4] = [8, 9]  # Assign a new sublist to a slice
print(nums)         # print(s "[0, 1, 8, 9, 4]"

## Loops
print("## Loops")
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

## List comprehensions
print("# List comprehensions")
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"