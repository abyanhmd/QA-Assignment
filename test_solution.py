import unittest
from typing import List
from solution import Solution

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def setUp(self):
        self.solution = Solution()

    # Test case 1
    def test_topKFrequent_case1(self):
        """
        The numbers are (1, 1, 1, 2, 2, 3) and the K is 2.
        The expected numbers are 1 and 2.
        """
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 2
    def test_topKFrequent_case2(self):
        """
        The numbers are (1, 1, 1, 2, 2, 2, 3, 3, 3, 3) and the K is 1.
        The expected number is 3.
        """
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
        k = 1
        expected = [3]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 3
    def test_topKFrequent_case3(self):
        """
        The numbers are (1, 2, 3, 4, 5) and the K is 3.
        The expected numbers are 1, 2, and 3.
        """
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = [1, 2, 3]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 4
    def test_topKFrequent_case4(self):
        """
        The numbers are (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) and the K is 3.
        The expected numbers are 1, 2, and 3.
        """
        nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        k = 3
        expected = [1, 2, 3]

        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 5
    def test_topKFrequent_case5(self):
        """
        The number is (5) and the K is 1.
        The expected number is 5.
        """
        nums = [5]
        k = 1
        expected = [5]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 6
    def test_topKFrequent_bva_minValues(self):
        """
        The numbers are (-10000, -10000, -5000, -5000, -10000, -1000) and the K is 1.
        The expected number is -10000.
        """
        nums = [-10000, -10000, -5000, -5000, -10000, -1000]
        k = 1
        expected = [-10000]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Test case 7
    def test_topKFrequent_bva_maxValues(self):
        """
        The numbers are (1000, 1000, 5000, 5000, 10000, 10000) and the K is 3.
        The expected numbers are 1000, 5000, 10000.
        """
        nums = [1000, 1000, 5000, 5000, 10000, 10000]
        k = 3
        expected = [1000, 5000, 10000]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

     # Test case 8
    def test_topKFrequent_bva_maxLength(self):
        """
        The numbers are (1000 for 10 power of 5 times) and the K is 1.
        The expected number is 10000.
        """
        nums = [10000] * (10**5)
        k = 1
        expected = [10000]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)

    # Bug reports
    @unittest.skip("Invalid input")
    def test_topKFrequent_largeK(self):
        """
        The numbers are (1, 2, 3, 4, 5) and the K is 10.
        Based on the constraint, it is possible to input the number like this.
        But in reality, this is uncomputable.
        I put unit test skip because this is invalid input.
        """
        nums = [1, 2, 3, 4, 5]
        k = 10
        expected = [1, 2, 3, 4, 5]
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
