def handle_wildcard(counter,jumble):
    """
    Function to determine if wildcard chars in jumble,
    can be mapped to remaining letters

    Args:
        param1(str): jumble.
        param2(str): word.

    Returns:
        bool : 
        True if word can be formed, 
        False if non alphabet is found and cannot be substitued for wildcard.
    
    """
    for c in counter.elements():
        if not c.isalpha():
            return False
    return sum(counter.values()) <= jumble.count('?')