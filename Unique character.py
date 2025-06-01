def uni_char(s):
    return len(set(s)) == len(s)

#efficient solution
def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)
    return True
