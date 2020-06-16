"""
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. 
The car is supposed to get to the opposite, Northeast (top-right), corner of the grid. 
Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.

For convenience, let’s represent every square in the grid as a pair (i,j). The first coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis. 
The initial state of the car is (0,0), and the destination is (n-1,n-1).
The car must abide by the following two rules: it cannot cross the diagonal border. In other words, in every step the position (i,j) needs to maintain i >= j. 
See the illustration above for n = 5. In every step, it may go one square North (up), or one square East (right), but not both. 
E.g. if the car is at (3,1), it may go to (3,2) or (4,1).
Explain the correctness of your function, and analyze its time and space complexities.

Approach: DO NOT see the figure provided by Pramp

position is valid only if i >= j

   j
i  0  1  2  3
0  1  0  0  0
1  1  1  0  0
2  1  2  2  0
3  1  3  5  5

INIT
prev = [1, 0, 0, 0]
curr = [1, 0, 0, 0]
"""
def num_of_paths(n):
     prev = curr = [1] + [0] * (n - 1)

     for i in range(1, n):
          for j in range(1, n):
               if i >= j:
                    curr[j] = curr[j - 1] + prev[j]

     return prev[-1]
     
import unittest
class TestNumOfPaths(unittest.TestCase):
     def test_generic(self):
          self.assertEqual(num_of_paths(4), 5)

if __name__ == "__main__": unittest.main()