def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    
    return inverted

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 1}

result = invert_dict(dict1)
print("Inverted Dictionary:", result)