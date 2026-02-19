def is_paired(input_string):
    stack = []
    matching_pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in input_string:
        if char in matching_pairs:  # Opening bracket
            stack.append(char)
        elif char in matching_pairs.values():  # Closing bracket
            if not stack or matching_pairs[stack.pop()] != char:
                return False
        # All other characters are ignored
    
    return len(stack) == 0