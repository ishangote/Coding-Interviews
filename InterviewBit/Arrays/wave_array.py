"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

[1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
 NOTE : If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3] 
"""

def wave_array(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

import unittest
class TestWaveArray(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(wave_array([1]), [1])
    
    def test_generic(self):
        self.assertEqual(wave_array([5, 4, 1, 3, 2]), [2, 1, 4, 3, 5])

if __name__ == "__main__": unittest.main()