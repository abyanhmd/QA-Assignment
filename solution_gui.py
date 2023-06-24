import tkinter as tk
from solution import Solution

class TopKFrequentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Top K Frequent Elements")
        
        self.solution = Solution()

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.root, text="Enter numbers (comma-separated) :")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack()

        self.k_label = tk.Label(self.root, text="Enter value of K :")
        self.k_label.pack()

        self.k_entry = tk.Entry(self.root)
        self.k_entry.pack()

        self.find_button = tk.Button(self.root, text="Find", command=self.find_top_k_frequent)
        self.find_button.pack()

        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()

        self.result_text = tk.Text(self.root, height=5, width=30)
        self.result_text.pack()
        self.result_text.configure(state='disabled')

    def find_top_k_frequent(self):
        nums = self.input_entry.get().split(",")
        nums = [int(num.strip()) for num in nums]

        k = int(self.k_entry.get())

        try:
            result = self.solution.topKFrequent(nums, k)
            self.result_text.configure(state='normal')
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, ', '.join(map(str, result)))
            self.result_text.configure(state='disabled')
        
        except Exception as e:
            self.result_text.configure(state='normal')
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, str(e))
            self.result_text.configure(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = TopKFrequentGUI(root)
    root.mainloop()
