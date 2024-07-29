def merging_Dict(*args):
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

result = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", result)