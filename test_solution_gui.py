import unittest
from tkinter import Tk
from tkinter.constants import DISABLED, NORMAL
from tkinter import messagebox
import tkinter as tk
from unittest.mock import patch
from solution import Solution
from solution_gui import TopKFrequentGUI

class TestTopKFrequentGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = TopKFrequentGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_topKFrequentGUI_case1(self):
        self.app.input_entry.insert(tk.END, "1, 1, 1, 2, 2, 3")
        self.app.k_entry.insert(tk.END, "2")

        expected_result = [1, 2]

        with patch.object(Solution, 'topKFrequent', return_value=expected_result):
            self.app.find_top_k_frequent()

        self.assertEqual(self.app.result_text.get(1.0, tk.END).strip(), '1, 2')
        self.assertEqual(self.app.result_text['state'], DISABLED)

    def test_topKFrequentGUI_case2(self):
        self.app.input_entry.insert(tk.END, "1, 1, 1, 2, 2, 2, 3, 3, 3, 3")
        self.app.k_entry.insert(tk.END, "1")

        expected_result = [3]

        with patch.object(Solution, 'topKFrequent', return_value=expected_result):
            self.app.find_top_k_frequent()

        self.assertEqual(self.app.result_text.get(1.0, tk.END).strip(), "3")
        self.assertEqual(self.app.result_text['state'], DISABLED)

    def test_topKFrequentGUI_case3(self):
        self.app.input_entry.insert(tk.END, "1, 2, 3, 4, 5")
        self.app.k_entry.insert(tk.END, "3")

        expected_result = [1, 2, 3]

        with patch.object(Solution, 'topKFrequent', return_value=expected_result):
            self.app.find_top_k_frequent()

        self.assertEqual(self.app.result_text.get(1.0, tk.END).strip(), "1, 2, 3")
        self.assertEqual(self.app.result_text['state'], DISABLED)

    def test_topKFrequentGUI_case4(self):
        self.app.input_entry.insert(tk.END, "1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 2, 1")
        self.app.k_entry.insert(tk.END, "3")

        expected_result = [1, 2, 3]

        with patch.object(Solution, 'topKFrequent', return_value=expected_result):
            self.app.find_top_k_frequent()

        self.assertEqual(self.app.result_text.get(1.0, tk.END).strip(), "1, 2, 3")
        self.assertEqual(self.app.result_text['state'], DISABLED)

    def test_topKFrequentGUI_case5(self):
        self.app.input_entry.insert(tk.END, "5")
        self.app.k_entry.insert(tk.END, "1")

        expected_result = [5]

        with patch.object(Solution, 'topKFrequent', return_value=expected_result):
            self.app.find_top_k_frequent()

        self.assertEqual(self.app.result_text.get(1.0, tk.END).strip(), "5")
        self.assertEqual(self.app.result_text['state'], DISABLED)

if __name__ == '__main__':
    unittest.main()
