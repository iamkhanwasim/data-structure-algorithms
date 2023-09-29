## Validate subsequent array

# Question: 
# Given two non-empty array of integer, write a function that determines whether the second
# array is a subsequence of the first one. 

# A subsequent array is not necassarily addjacent to the first but is of the same order as 
# they appear in the first array

# Example:
# array = [3, 7, 12, 4, 1, 9, 5, 10]
# subsequentarray = [7, 4, 9, 10]

# Solution 1: using while loop
# Space complexity: O(n), as iterated through Array(array)
# Time complexity: O(1), as iterated through Array(array)
def is_valid_subsequence(array, subsequence):
    seqIdx = 0
    arrIdx = 0

    # This condition is true and loop will break when condition fails
    while len(array) > arrIdx and (len(subsequence) > seqIdx):  
        # if the element in sequence[] matches the element in an array, then the seqindex is incremented
        # and looks for the next element in subsequence
        if subsequence[seqIdx] == array[arrIdx]: 
            seqIdx += 1

        # array index is icremented regardless of any matches
        arrIdx += 1

    return seqIdx == len(subsequence) # if the subsequnce has been traversed


# Solution 2: Using for loop
# Space complexity: O(n), as iterated through Array(array)
# Time complexity: O(1), as iterated through Array(array)
def is_valid_subsequence(array, subsequence):
    seqIdx = 0

    # Iterate through the array to find a match of element
    for arrIdx in array:
        # if the element in sequence[] matches the element in an array, then the seqindex is incremented
        # and looks for the next element in subsequence
        if subsequence[seqIdx] == arrIdx:
            seqIdx += 1
        if seqIdx == len(subsequence):
            break

    # if the subsequnce has been traversed
    return seqIdx == len(subsequence)


# print(isValidSubsequence([3, 7, 12, 4, 1, 9, 5, 10], [7, 4, 9, 10]))

# Unit testing  
import unittest
class TestCode(unittest.TestCase):
    def test_valid_sequence(self):
        array, sequence = [3, 7, 12, 4, 1, 9, 5, 10], [7, 4, 9, 10]
        result = is_valid_subsequence(array, sequence)
        self.assertEqual(result, True)

    def test_invalid_sequence(self):
        array, sequence = [3, 7, 12, 4, 1, 9, 5, 10], [1,2,6,8]
        result = is_valid_subsequence(array, sequence)
        self.assertEqual(result, False)

    def test_invalid_array(self):
        array, sequence = [3, 7, 12, '4', 1, 9, 5, 10], [1,2,6,8]
        result = is_valid_subsequence(array, sequence)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()