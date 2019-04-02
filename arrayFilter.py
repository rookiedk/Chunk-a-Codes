"""
Function that takes two arrays of strings as arguments and
returns a filtered array of items only in array1 and not in array2
"""

def arrayFilter(array1, array2):
    """
    :param array1: input array with strings
    :param array2: array to be compared against
    :return: new filtered array, not containing strings
    """
    return list(filter(lambda n: n not in array2, array1))

# Example 1 - works with number arrays:
array1 = [1,2,3,4]
array2 = [2,3]
filtered_array_int = arrayFilter(array1, array2) # returns [1,4]

# Example 1 - works with string arrays:
array1 = ['Mallard', 'Hook Bill', 'African', 'Crested', 'Pilgrim', 'Toulouse', 'Blue Swedish']
array2 = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']
filtered_array_str = arrayFilter(array1, array2) # returns ['Mallard', 'Hook Bill', 'Crested', 'Blue Swedish']

