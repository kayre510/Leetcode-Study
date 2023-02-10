# Binary Search

def binary_search(items, target):
  # Initialize the start and end indices
  start = 0
  end = len(items) - 1

  # While the start index is less than or equal to the end index:
  while start <= end:
    # Calculate the middle index
    middle = (start + end) // 2

    # If the element at the middle index is less than the target:
    if items[middle] < target:
      # Set the start index to the element after the middle index
      start = middle + 1
    # If the element at the middle index is greater than the target:
    elif items[middle] > target:
      # Set the end index to the element before the middle index
      end = middle - 1
    # If the element at the middle index is equal to the target:
    else:
      # Return the middle index
      return target

  # If the target is not found, return None
  return None


