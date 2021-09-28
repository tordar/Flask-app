import numpy as np
import matplotlib.pyplot
from flask import Flask, render_template

application = Flask(__name__)

x = 'Hello world, from flask'

print('Hello from python')

a=np.zeros(4)
print(a)

@application.route('/')
def homepage():
    return render_template('index.html', y=x)



application.run()

