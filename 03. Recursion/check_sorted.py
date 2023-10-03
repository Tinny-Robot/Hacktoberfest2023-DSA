def is_sorted(arr):
    """
    Check if the given array is sorted in non-decreasing order.
    
    Args:
    arr (list): The input list to be checked.
    
    Returns:
    bool: True if the array is sorted, False otherwise.
    """
    # Base case: If the array has 0 or 1 element, it is considered sorted.
    if len(arr) <= 1:
        return True
    
    # Recursive case: Check if the first element is greater than the second element.
    # If it is, the array is not sorted.
    if arr[0] > arr[1]:
        return False
    
    # Recursively check the rest of the array (excluding the first element).
    return is_sorted(arr[1:])
