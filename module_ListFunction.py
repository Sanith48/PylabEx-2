def find_max(lst):
    """Returns the maximum value in the list."""
    if not lst:
        raise ValueError("The list is empty.")
    return max(lst)

def find_min(lst):
    """Returns the minimum value in the list."""
    if not lst:
        raise ValueError("The list is empty.")
    return min(lst)

def calculate_sum(lst):
    """Returns the sum of all elements in the list."""
    if not lst:
        return 0
    return sum(lst)
def calculate_average(lst):
    """Returns the average of the list."""
    if not lst:
        raise ValueError("The list is empty.")
    return sum(lst) / len(lst)

def find_median(lst):
    """Returns the median of the list."""
    if not lst:
        raise ValueError("The list is empty.")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]