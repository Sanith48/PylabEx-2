def add_element(s, element):
    """Add an element to a set. Do nothing if the element exists"""
    s.add(element)

def remove_element(s, element):
    """Remove an element from a set. Do nothing, if the element is not present."""
    s.discard(element)  
def union_sets(s1, s2):
    """Return the union of two sets."""
    return s1.union(s2)

def intersection_sets(s1, s2):
    """Return the intersection of two sets."""
    return s1.intersection(s2)

def difference_sets(s1, s2):
    """Return the difference of two sets (s1 - s2)."""
    return s1.difference(s2)

def is_subset(s1, s2):
    """Check if set s1 is a subset of set s2."""
    return s1.issubset(s2)

def set_length(s):
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference_sets(s1, s2):
    """Compute the symmetric difference of two sets."""
    return s1.symmetric_difference(s2)

def power_set(s):
    """Compute the power set of a given set."""
    power_set_result = [[]]
    for elem in s:
        power_set_result += [subset + [elem] for subset in power_set_result]
    return [set(subset) for subset in power_set_result]

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    from itertools import combinations
    subsets = []
    for r in range(len(s) + 1):
        subsets.extend(set(combinations(s, r)))
    return subsets