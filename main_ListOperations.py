# main_ListOperations.py

import module_ListFunction

def demo_functions():
    # Example lists
    list1 = [10, 20, 30, 40, 50]
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    list3 = [7, 1, 3, 4, 2, 6, 8]

    # Demonstrating functions
    print("List 1:", list1)
    print("Max of List 1:", module_ListFunction.find_max(list1))
    print("Min of List 1:", module_ListFunction.find_min(list1))
    print("Sum of List 1:", module_ListFunction.calculate_sum(list1))
    print("Average of List 1:", module_ListFunction.calculate_average(list1))
    print("Median of List 1:", module_ListFunction.find_median(list1))
    
    print("\nList 2:", list2)
    print("Max of List 2:", module_ListFunction.find_max(list2))
    print("Min of List 2:", module_ListFunction.find_min(list2))
    print("Sum of List 2:", module_ListFunction.calculate_sum(list2))
    print("Average of List 2:", module_ListFunction.calculate_average(list2))
    print("Median of List 2:", module_ListFunction.find_median(list2))
    
    print("\nList 3:", list3)
    print("Max of List 3:", module_ListFunction.find_max(list3))
    print("Min of List 3:", module_ListFunction.find_min(list3))
    print("Sum of List 3:", module_ListFunction.calculate_sum(list3))
    print("Average of List 3:", module_ListFunction.calculate_average(list3))
    print("Median of List 3:", module_ListFunction.find_median(list3))

if __name__ == "__main__":
    demo_functions()