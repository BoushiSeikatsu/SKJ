def is_palindrome(data):
    """
    Returns True if `data` is a palindrome and False otherwise.
    Hint:
        slicing is your friend, use it
    Example:
        is_palindrome('aba') == True
        is_palindrome('abc') == False
    """
    for i in range(0, len(data)):
        forwardReading = data[i]
        backwardReading = data[-(i+1)]
        if(forwardReading != backwardReading):
            return False
    return True
#data = "abba"
#result = is_palindrome(data)
def lex_compare(a, b):
    """
    Lexicographically compare `a` with `b` and return the smaller string.
    Implement the comparison yourself, do not use the `<` operator for comparing strings :)

    Example:
        lex_compare('a', 'b') == 'a'
        lex_compare('ahoj', 'buvol') == 'ahoj'
        lex_compare('ahoj', 'ahojky') == 'ahoj'
        lex_compare('dum', 'automobil') == 'automobil'
    """
    #a = 'dum'
    #b = 'automobil'
    shorterStringLength = ((len(a),len(b)) [len(b) < len(a)])
    for i in range(0,shorterStringLength):
        if(a[i] < b[i]):
            return a
        elif(a[i] > b[i]):
            return b
    return ((a, b) [len(b) < len(a)])


def count_successive(string):
    """
    Go through the string and for each character, count how many times it appears in succession.
    Store the character and the count in a tuple and return a list of such tuples.

    Example:
          count_successive("aaabbcccc") == [("a", 3), ("b", 2), ("c", 4)]
          count_successive("aba") == [("a", 1), ("b", 1), ("a", 1)]
    """
    if(len(string) == 0):
        return []
    result = []
    lastChar = string[0]
    result.append((lastChar,0))#First char is gonna increment it
    for char in string:
        if(lastChar == char):
            result[-1] = (lastChar,result[-1][1]+1)
        else:
            lastChar = char
            result.append((lastChar,1))
    return result

def find_positions(items):
    """
    Go through the input list of items and collect indices of each individual item.
    Return a dictionary where the key will be an item and its value will be a list of indices
    where the item was found.

    Example:
        find_positions(["hello", 1, 1, 2, "hello", 2]) == {
            2: [3, 5],
            "hello": [0, 4],
            1: [1, 2]
        }
    """
    result = dict()
    for i in range(0, len(items)):
        if(items[i] not in result.keys()):
            result.update({items[i]: []})
        result[items[i]].append(i)
    return result


def invert_dictionary(dictionary):
    """
    Invert the input dictionary. Turn keys into values and vice-versa.
    If more values would belong to the same key, return None.

    Example:
        invert_dictionary({1: 2, 3: 4}) == {2: 1, 4: 3}
        invert_dictionary({1: 2, 3: 2}) is None
    """
    
    result = dict()
    for key, value in dictionary.items():
        if(value not in result.keys()):
            result.update({value: key})
        else:
            return None
    return result
#dictionary = {1: 2, 3: 2}
#output = invert_dictionary(dictionary)