def find_combinations(inputarray, target, current_combination=[], index=0, max_sum=4500):
    """
    Finds all possible combinations of elements from the input list that sum up to the target value
    and where the total sum of the chosen combination is less than max_sum.

    Args:
        inputarray: The list of elements to choose from.
        target: The target sum to achieve.
        current_combination: The current combination being built.
        index: The index of the current element being considered.
        max_sum: The maximum allowed sum for the chosen combination.

    Returns:
        A list of all possible combinations.
    """
    if target == 0 and sum(current_combination) < max_sum:
        return [current_combination]

    if target < 0 or index >= len(inputarray):
        return []

    # Include the current element in the combination
    combinations_with_current = find_combinations(
        inputarray, target - inputarray[index], current_combination + [inputarray[index]], index, max_sum
    )

    # Exclude the current element from the combination
    combinations_without_current = find_combinations(
        inputarray, target, current_combination, index + 1, max_sum
    )

    return combinations_with_current + combinations_without_current


# Input from the user
num = int(input("How many numbers do you have? "))
inputarray = []
for i in range(num):
    inputarray.append(int(input(f"Enter number {i + 1}: ")))

target = int(input("The target sum is: "))

# Find combinations
combinations = find_combinations(inputarray, target)
print("Combinations that sum to the target and have a total sum less than", target, ":")
print(combinations)
