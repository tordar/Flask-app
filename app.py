import numpy as np
from flask import Flask, render_template



x = 'Hello world, from flask'

print('Hello from python')

a=np.zeros(4)
print(a)


def create_app():
    application = Flask(__name__)
    @application.route('/')
    def homepage():
        return render_template('index.html', y=x)

    return application


if __name__ == "__main__":
    application = create_app()
    application.run(host='0.0.0.0', debug=True)
