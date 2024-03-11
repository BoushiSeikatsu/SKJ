# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:38:19 2024

@author: Michal
"""

import dataclasses
from typing import Callable, Generic, List, Optional, TypeVar


def cached(f):
    """
    Create a decorator that caches up to 3 function results, based on the same parameter values.

    When `f` is called with the same parameter values that are already in the cache, return the
    stored result associated with these parameter values. You can assume that `f` receives only
    positional arguments (you can ignore keyword arguments).

    When `f` is called with new parameter values, forget the oldest inserted result in the cache
    if the cache is already full.

    Example:
        @cached
        def fn(a, b):
            return a + b # imagine an expensive computation

        fn(1, 2) == 3 # computed
        fn(1, 2) == 3 # returned from cache, `a + b` is not executed
        fn(3, 4) == 7 # computed
        fn(3, 5) == 8 # computed
        fn(3, 6) == 9 # computed, (1, 2) was now forgotten
        fn(1, 2) == 3 # computed again, (3, 4) was now forgotten
    """
    queue = []
    def inner(*args, **kwargs):
        for memory in queue:
            if(memory[0] == args[0] and memory[1] == args[1]):#Is cached
                print("Returned from cache")
                return memory[2]
            elif(len(queue) != 3):#Isnt cached and queue isnt full
                queue.append((args[0],args[1],f(*args, **kwargs)))
            else:#Isnt cached and queue is full
                queue.pop(0)
                queue.append((args[0],args[1],f(*args, **kwargs)))
        if(len(queue) == 0):#First call of function
            queue.append((args[0],args[1],f(*args, **kwargs)))
        return queue[-1][2]
    return inner
    pass
@cached
def fn(a, b):
    return a + b
#print(fn(1,2))
#print(fn(1,2))
T = TypeVar("T")


@dataclasses.dataclass
class ParseResult(Generic[T]):
    """
    Represents result of a parser invocation.
    If `value` is `None`, then the parsing was not successful.
    `rest` contains the rest of the input string if parsing was succesful.
    """
    value: Optional[T]
    rest: str

    @staticmethod
    def invalid(rest: str) -> "ParseResult":
        return ParseResult(value=None, rest=rest)

    def is_valid(self) -> bool:
        return self.value is not None


"""
Represents a parser: a function that takes a string as an input and returns a `ParseResult`.
"""
Parser = Callable[[str], ParseResult[T]]

"""
Below are functions that create new parsers.
They should serve as LEGO blocks that can be combined together to build more complicated parsers.
See tests for examples of usage.

Note that parsers are always applied to the beginning of the string:
```python
parser = parser_char("a")
parser("a")  # ParseResult(value="a", rest="")
parser("xa") # ParseResult(value=None, rest="xa")
```
"""



def parser_char(char: str) -> Parser[str]:
    """
    Return a parser that will parse a single character, `char`, from the beginning of the input
    string.

    Example:
        ```python
        parser_char("x")("x") => ParseResult(value="x", rest="")
        parser_char("x")("xa") => ParseResult(value="x", rest="a")
        parser_char("y")("xa") => ParseResult(value=None, rest="xa")
        ```
    """
    def parse(input_str: str) -> ParseResult[str]:
        if input_str.startswith(char):
            return ParseResult(value=char, rest=input_str[len(char):])
        else:
            return ParseResult.invalid(input_str)

    return parse    

"""
def parser(func):
    def inner(*args):
        result = func(*args)
"""

def parser_repeat(parser: Parser[T]) -> Parser[List[T]]:
    """
    Return a parser that will invoke `parser` repeatedly, while it still matches something in the
    input.

    Example:
        ```python
        parser_a = parser_char("a")
        parser = parser_repeat(parser_a)
        parser("aaax") => ParseResult(value=["a", "a", "a"], rest="x")
        parser("xa") => ParseResult(value=[], rest="xa")
        ```
    """
    def parse(inputString: str):
        resultOfParse = parser(inputString)
        resultOfFunc = ParseResult([], "")
        while(resultOfParse.value is not None):
            resultOfFunc.value.append(resultOfParse.value)
            resultOfFunc.rest = resultOfParse.rest
            resultOfParse = parser(resultOfParse.rest)
        if(len(resultOfFunc.value) == 0):
            resultOfFunc.rest = resultOfParse.rest
        return resultOfFunc
    return parse
def parser_seq(parsers: List[Parser]) -> Parser:
    """
    Create a parser that will apply the given `parsers` successively, one after the other.
    The result will be successful only if all parsers succeed.

    Example:
        ```python
        parser_a = parser_char("a")
        parser_b = parser_char("b")
        parser = parser_seq([parser_a, parser_b, parser_a])
        parser("abax") => ParseResult(value=["a", "b", "a"], rest="x")
        parser("ab") => ParseResult(value=None, rest="ab")
        ```
    """
    def parse(inputString: str):
        resultOfFunc = ParseResult([],inputString)
        for parser in parsers:
            resultOfParse = parser(resultOfFunc.rest)
            if(resultOfParse.value is None):
                resultOfFunc = ParseResult(None, inputString)
                break
            else:
                resultOfFunc.value.append(resultOfParse.value)
                resultOfFunc.rest = resultOfParse.rest
        return resultOfFunc
    return parse

def parser_choice(parsers: List[Parser]) -> Parser:
    """
    Return a parser that will return the result of the first parser in `parsers` that matches something
    in the input.

    Example:
        ```python
        parser_a = parser_char("a")
        parser_b = parser_char("b")
        parser = parser_choice([parser_a, parser_b])
        parser("ax") => ParseResult(value="a", rest="x")
        parser("bx") => ParseResult(value="b", rest="x")
        parser("cx") => ParseResult(value=None, rest="cx")
        ```
    """
    def parse(inputString: str):
        for parser in parsers:
            returnOfParser = parser(inputString)
            if(returnOfParser.value is not None):
                return returnOfParser
        return ParseResult(None, inputString)
    return parse

R = TypeVar("R")


def parser_map(parser: Parser[R], map_fn: Callable[[R], Optional[T]]) -> Parser[T]:
    """
    Return a parser that will use `parser` to parse the input data, and if it is successful, it will
    apply `map_fn` to the parsed value.
    If `map_fn` returns `None`, then the parsing result will be invalid.

    Example:
        ```python
        parser_a = parser_char("a")
        parser = parser_map(parser_a, lambda x: x.upper())
        parser("ax") => ParseResult(value="A", rest="x")
        parser("bx") => ParseResult(value=None, rest="bx")

        parser = parser_map(parser_a, lambda x: None)
        parser("ax") => ParseResult(value=None, rest="ax")
        ```
    """
    def parse(inputString: str):
        resultOfParser = parser(inputString)
        if(resultOfParser.value is not None):
            resultOfParser.value = map_fn(resultOfParser.value)
        if(resultOfParser.value is None):
            resultOfParser.rest = inputString
        return resultOfParser
    return parse 

def parser_matches(filter_fn: Callable[[str], bool]) -> Parser[str]:
    """
    Create a parser that will parse the first character from the input, if it is accepted by the
    given `filter_fn`.

    Example:
        ```python
        parser = parser_matches(lambda x: x in ("ab"))
        parser("ax") => ParseResult(value="a", rest="x")
        parser("bx") => ParseResult(value="b", rest="x")
        parser("cx") => ParseResult(value=None, rest="cx")
        parser("") => ParseResult(value=None, rest="")
        ```
    """
    def parse(inputString: str):
        if(len(inputString) == 0):
            return ParseResult(None, inputString)
        if(filter_fn(inputString[0])):
            value, rest = inputString[0], inputString[1::]
            return ParseResult(value, rest)
        else:
            return ParseResult(None, inputString)
    return parse
# Use the functions above to implement the functions below.
parser = parser_matches(lambda x: x in ("ab"))
print(parser("ax")) #=> ParseResult(value="a", rest="x")
print(parser("bx")) #=> ParseResult(value="b", rest="x")
print(parser("cx")) #=> ParseResult(value=None, rest="cx")
print(parser("")) #=> ParseResult(value=None, rest="")

def parser_string(string: str) -> Parser[str]:
    """
    Create a parser that will parse the given `string`.

    Example:
        ```python
        parser = parser_string("foo")
        parser("foox") => ParseResult(value="foo", rest="x")
        parser("fo") => ParseResult(value=None, rest="fo")
        ```
    """


def parser_int() -> Parser[int]:
    """
    Create a parser that will parse a non-negative integer (you don't have to deal with
    `-` at the beginning).

    Example:
        ```python
        parser = parser_int()
        parser("123x") => ParseResult(value=123, rest="x")
        parser("foo") => ParseResult(value=None, rest="foo")
        ```
    """