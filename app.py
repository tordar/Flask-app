import numpy as np
from flask import Flask, render_template, jsonify


application = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    application.debug = True
else:
    application.debug = False

random_decimal = np.random.rand()
@application.route('/update', methods=['POST'])
def update():
    random_decimal = np.random.rand()
    return jsonify('', render_template('random_decimal_model.html', x=random_decimal))

@application.route('/')
def homepage():
    return render_template('index.html', x=random_decimal)

if __name__ == "__main__":
    application.run()
