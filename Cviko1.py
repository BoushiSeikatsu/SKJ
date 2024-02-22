"""
Script for the first laboratory.
Add code by following instructions of the teacher.
"""

def add(a, b):
    """Adds parameters."""
    return a + b

def what_number(number):
    """Returns string positive/zero/negative specifying
    value of the number."""
    if (number > 0):
        return "positive"
    elif (number < 0):
        return "negative"
    else:
        return "zero"
    pass

def sum_of_numbers(numbers):
    totalSum = 0
    for number in numbers:
        totalSum += number
    return totalSum
    pass

def ship_name(fleet, designated_no):
    """Return ship's name for specified designated number
    from the fleet."""
    if designated_no in fleet:
        return fleet[designated_no]
    else:
        "Wrong designated number"
    pass

def how_many_5(numbers, threshold = 5):
    """Returns number of numbers greater than 5."""
    countOfGreat = 0
    for number in numbers:
        if(number > threshold):
            countOfGreat += 1
    return countOfGreat
    # Modify example to take argument that specifies threshold
    pass

def gen_list_gt(lst, no):
    """Returns list with numbers greater than no."""
    result = []
    for number in lst:
        if(number > no):
            result.append(number)
    return result
    #syntax: [ item for item in lst if_condition ]
    pass

print(add(1, 3))
print(add([1, 2, 3], [4, 5, 6]))
# Try addition of strings or different data type and see what happens

#if statement example
n = 5
print("Number", n, "is:", what_number(n))

#for example: sum of the list example
lst = [1, 2, 3, 6, 7, 8]
print("Sum is:", sum_of_numbers(lst))

#dictionary example
fleet = {'BS62': 'Pegasus', "BS75": "Galactica", 36: 'Valkirie'}
designated_no = "BS62"
print("We've got {} in the fleet".format(ship_name(fleet, designated_no)))

#function to count how many numbers > 5 are in the list
lst = [1, 2, 5, 6, 7, 10, 12, 40, 3]
print("There are {} numbers greater than 5".format(how_many_5(lst)))

#generating list example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
no = 5
print("List with numbers > {}: {}".format(no, gen_list_gt(lst, no)))