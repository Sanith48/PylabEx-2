def common_keys(*args):
    if not args:
        return set()
    
    common = set(args[0].keys())
    for d in args[1:]:
        common.intersection_update(d.keys())
    
    return common

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'b': 7, 'c': 8, 'e': 9}

result = common_keys(dict1, dict2, dict3)
print("Common Keys:", result)