def solution(s):
    # check string length and add '_'
    if len(s) % 2 != 0:
        s += '_'
    
    # create a list of pairs
    pairs = []
    
    # loop through string
    for i in range(0, len(s), 2):
        # slicing strings into chunks of 2 characters
        pairs.append(s[i:i+2])
        
    return pairs
