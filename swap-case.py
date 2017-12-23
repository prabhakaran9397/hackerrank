def swap_case(s):
    ''' 
    using in-built
    import string
    return string.swapcase(s)
    '''
    
    ''' using chr, ord '''
    return "".join(map(lambda c: chr(ord(c)^32) if c.isalpha() else c, s))
