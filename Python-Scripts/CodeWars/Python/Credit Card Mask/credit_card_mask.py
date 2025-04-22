# return masked string
def maskify(cc):
    # return string if length is 4 or less
    if len(cc) <= 4:
        return cc
    
    # find the number of characters #
    string_len = len(cc) - 4
    
    # create masked string
    masked_part = '#' * string_len
    visible_part = cc[-4:]
    
    return masked_part + visible_part
