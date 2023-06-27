from flask import Flask, render_template, request
from typing import List
from solution import Solution

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    solution = Solution()

    if request.method == 'POST':
        nums = request.form.get('nums')
        k = request.form.get('k')

        nums_list = list(map(int, nums.split(',')))
        k = int(k)

        solution = Solution()
        result = solution.topKFrequent(nums_list, k)

        return render_template('index.html', result=result)

    return render_template('./index.html')

if __name__ == '__main__':
    app.run()
