def common_key_value_pairs(*args):
    if not args:
        return set()
    
    common = set(args[0].items())
    for d in args[1:]:
        common.intersection_update(d.items())
    
    return common

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
dict3 = {'b': 2, 'c': 3, 'e': 5}

result = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", result)