from flask import Flask, render_template
from linear_regression import LinearRegression
from make_sample import MakeSample

app = Flask(__name__)


@app.route('/')
def return_hello():
    return render_template('result.html')


m = MakeSample()
m.make_sample()
l = LinearRegression()
l.work()

app.run(host="0.0.0.0", port=8080, debug=True)
