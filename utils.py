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
            """
            The problem defenition states wildcards can be mapped only to 26 alphabets
            hence if the remainder of counter contains any punctuation it cannot be mapped 
            hence return false
            """
            return False
    return sum(counter.values()) <= jumble.count('?')