from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = int(request.form['number'])
        factorial = calculate_factorial(number)
        calculations = []
        for i in range(number, 0, -1):
            calculations.append(str(i))
        return render_template('index.html', factorial=factorial, calculations=calculations)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
