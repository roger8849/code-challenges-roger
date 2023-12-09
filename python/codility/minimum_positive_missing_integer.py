def find_minimum_positive(arr):
    # Create a set to store unique positive integers
    positive_integers = set()

    # Iterate through the array and add positive integers to the set
    for num in arr:
        if num > 0:
            positive_integers.add(num)

    # Find the minimum positive integer
    min_positive = 1
    while min_positive in positive_integers:
        min_positive += 1

    return min_positive

# Example usage:
arr = [3, 5, 1, -2, 2, 6]
result = find_minimum_positive(arr)
print("Minimum positive integer:", result)



arr = [-3,-2,-1,-2,-6]
result = find_minimum_positive(arr)
print("Minimum positive integer:", result)