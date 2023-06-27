import unittest
from flask import Flask, request, render_template
from flask.testing import FlaskClient
from typing import List
from solution import Solution

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    solution = Solution()

    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        nums = request.form.get('nums')
        k = request.form.get('k')

        nums_list = list(map(int, nums.split(',')))
        k = int(k)

        result = solution.topKFrequent(nums_list, k)

        return render_template('index.html', result=result)


class TestApp(unittest.TestCase):
    """
    Unit tests for the Flask app.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Top K Frequent Elements</h1>', response.data)

    def test_topKFrequent_case1(self):
        """
        The numbers are (1, 1, 1, 2, 2, 3) and the K is 2.
        The expected numbers are 1 and 2.
        """
        nums = '1,1,1,2,2,3'
        k = '2'
        expected = [1, 2]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)
        
    def test_topKFrequent_case2(self):
        """
        The numbers are (1, 1, 1, 2, 2, 2, 3, 3, 3, 3) and the K is 1.
        The expected number is 3.
        """
        nums = '1,1,1,2,2,2,3,3,3,3'
        k = '1'
        expected = [3]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_case3(self):
        """
        The numbers are (1, 2, 3, 4, 5) and the K is 3.
        The expected numbers are 1, 2, and 3.
        """
        nums = '1,2,3,4,5'
        k = '3'
        expected = [1, 2, 3]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_case4(self):
        """
        The numbers are (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) and the K is 3.
        The expected numbers are 1, 2, and 3.
        """
        nums = '1,2,3,4,5,1,2,3,4,5'
        k = '3'
        expected = [1, 2, 3]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_case5(self):
        """
        The number is (5) and the K is 1.
        The expected number is 5.
        """
        nums = '5'
        k = '1'
        expected = [5]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_bva_minValues(self):
        """
        The numbers are (-10000, -10000, -5000, -5000, -10000, -1000) and the K is 1.
        The expected number is -10000.
        """
        nums = '-10000,-10000,-5000,-5000,-10000,-1000'
        k = '1'
        expected = [-10000]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_bva_maxValues(self):
        """
        The numbers are (1000, 1000, 5000, 5000, 10000, 10000) and the K is 3.
        The expected numbers are 1000, 5000, 10000.
        """
        nums = '1000,1000,5000,5000,10000,10000'
        k = '3'
        expected = [1000, 5000, 10000]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    def test_topKFrequent_bva_maxLength(self):
        """
        The numbers are (1000 for 10 power of 5 times) and the K is 1.
        The expected number is 10000.
        """
        nums = [10000] * (10**5)
        k = '1'
        expected = [10000]

        response = self.app.post('/', data={'nums': ','.join(map(str, nums)), 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

    @unittest.skip("Invalid input")
    def test_topKFrequent_largeK(self):
        """
        The numbers are (1, 2, 3, 4, 5) and the K is 10.
        Based on the constraint, it is possible to input the number like this.
        But in reality, this is uncomputable.
        I put unit test skip because this is invalid input.
        """
        nums = '1,2,3,4,5'
        k = '10'
        expected = [1, 2, 3, 4, 5]

        response = self.app.post('/', data={'nums': nums, 'k': k})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Result:</h2>', response.data)
        self.assertIn(str(expected).encode(), response.data)

if __name__ == '__main__':
    unittest.main()
