# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 06:32:13 2024

@author: Michal
"""

def fizzbuzz(num):
    """
    Return 'Fizz' if `num` is divisible by 3, 'Buzz' if `num` is divisible by 5, 'FizzBuzz' if `num` is divisible both by 3 and 5.
    If `num` isn't divisible neither by 3 nor by 5, return `num`.
    Example:
        fizzbuzz(3) # Fizz
        fizzbuzz(5) # Buzz
        fizzbuzz(15) # FizzBuzz
        fizzbuzz(8) # 8
    """
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 5 == 0):
        return "Buzz"
    elif (num % 3 == 0):
        return "Fizz"
    else:
        return num
    pass


def fibonacci(n):
    """
    Return the `n`-th Fibonacci number (counting from 0).
    Example:
        fibonacci(0) == 0
        fibonacci(1) == 1
        fibonacci(2) == 1
        fibonacci(3) == 2
        fibonacci(4) == 3
    """
    #n = 1
    if(n == 1):
        return 1
    prelastNumber = 0
    lastNumber = 1
    result = 0
    for number in range(1,n):
        result = prelastNumber + lastNumber
        prelastNumber = lastNumber
        lastNumber = result
    return result
    pass


def dot_product(a, b):
    """
    Calculate the dot product of `a` and `b`.
    Assume that `a` and `b` have same length.
    Hint:
        lookup `zip` function
    Example:
        dot_product([1, 2, 3], [0, 3, 4]) == 1*0 + 2*3 + 3*4 == 18
    """
    #a = [1, 2, 3]
    #b = [0, 3, 4]
    zipped = zip(a,b)
    result = 0
    for left, right in zipped:
        result += left*right
    return result
    pass


def redact(data, chars):
    """
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case sensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # Sxcrxt xxxxagx
    """
    #data = "Hello world!"
    #chars = "lo"
    for char in chars:
        data = data.replace(char,'x')
    return data
    pass


def count_words(data):
    """
    Return a dictionary that maps word -> number of occurences in `data`.
    Words are separated by spaces (' ').
    Characters are case sensitive.

    Hint:
        "hi there".split(" ") -> ["hi", "there"]

    Example:
        count_words('this car is my favourite what car is this')
        {
            'this': 2,
            'car': 2,
            'is': 2,
            'my': 1,
            'favourite': 1,
            'what': 1
        }
    """
    #data = "this car is my favourite what car is this"
    if(data == ""):
        return {}
    splitString = data.split(" ")
    wordCountDict = dict()
    for word in splitString:
        if(word in wordCountDict):
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1
    return wordCountDict
    pass


def bonus_fizzbuzz(num):
    """
    Implement the `fizzbuzz` function.
    `if`, match-case and cycles are not allowed.
    """
    #num = 15
    emptyString = ""
    fizz = "Fizz"
    buzz = "Buzz"
    #Rozhodl jsem se pouzit touple ternalni operator
    result = ((emptyString, fizz) [num % 3 == 0])
    result += ((emptyString, buzz) [num % 5 == 0])
    result = ((result, num) [result == ""])
    return result
    pass


def bonus_utf8(cp):
    """
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Základy číslicových systémů (ZDS)`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
    """
    if cp < 0x80:
        # Single-byte encoding
        return bytes([cp])
    elif cp < 0x800:
        # Two-byte encoding
        byte1 = 0xC0 | (cp >> 6)
        byte2 = 0x80 | (cp & 0x3F)
        return bytes([byte1, byte2])
    elif cp < 0x10000:
        # Three-byte encoding
        byte1 = 0xE0 | (cp >> 12)
        byte2 = 0x80 | ((cp >> 6) & 0x3F)
        byte3 = 0x80 | (cp & 0x3F)
        return bytes([byte1, byte2, byte3])
    elif cp < 0x110000:
        # Four-byte encoding
        byte1 = 0xF0 | (cp >> 18)
        byte2 = 0x80 | ((cp >> 12) & 0x3F)
        byte3 = 0x80 | ((cp >> 6) & 0x3F)
        byte4 = 0x80 | (cp & 0x3F)
        return bytes([byte1, byte2, byte3, byte4])

# Example usage
unicode_code_point = 0x1F601  # Example code point for a smiling face emoji
utf8_bytes = bonus_utf8(unicode_code_point)
print("UTF-8 Bytes:", utf8_bytes)