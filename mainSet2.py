

from Set_Operations2 import (add_element, remove_element, union_sets, intersection_sets,
                            difference_sets, is_subset, set_length, symmetric_difference_sets,
                            power_set, unique_subsets)

def main():
    # Example sets
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    # Adding lement
    add_element(set1, 4)
    print(f"After adding 4 to set1: {set1}")

    # to remove element
    remove_element(set1, 2)
    print(f"After removing 2 from set1: {set1}")

    # find union of sets
    print(f"Union of set1 and set2: {union_sets(set1, set2)}")

    # find intersection of sets
    print(f"Intersection of set1 and set2: {intersection_sets(set1, set2)}")

    # find difference of sets
    print(f"Difference of set1 - set2: {difference_sets(set1, set2)}")

    # check is_subset
    print(f"Is set1 a subset of set2? {is_subset(set1, set2)}")

    # find the length of a set
    print(f"Length of set1: {set_length(set1)}")

    # finding symmetric difference of sets
    print(f"Symmetric difference of set1 and set2: {symmetric_difference_sets(set1, set2)}")

    # find power_set
    print(f"Power set of set1: {power_set(set1)}")

    # find unique_subsets
    print(f"Unique subsets of set1: {unique_subsets(set1)}")

if __name__ == "_main_":
    main()
    
    