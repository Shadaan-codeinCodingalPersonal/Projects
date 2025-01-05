# find the sum of numbers from set of numbers combination that gives sum of 500 and also the total sum for the chosen set of number shall be less than 4500
def find_combinations(input, target, current_combination=[], index=0):
  """
  Finds all possible combinations of elements from the input list that sum up to the target value.

  Args:
    input: The list of elements to choose from.
    target: The target sum to achieve.
    current_combination: The current combination being built.
    index: The index of the current element being considered.

  Returns:
    A list of all possible combinations.
  """
  if target == 0:
    return [current_combination]

  if target < 0 or index >= len(input):
    return []

  # Include the current element in the combination
  combinations_with_current = find_combinations(
      input, target - input[index], current_combination + [input[index]], index
  )

  # Exclude the current element from the combination
  combinations_without_current = find_combinations(
      input, target, current_combination, index + 1
  )

  return combinations_with_current + combinations_without_current


input = [11, 22, 33, 44, 10, 34]
target = 44
combinations = find_combinations(input, target)
print(combinations)