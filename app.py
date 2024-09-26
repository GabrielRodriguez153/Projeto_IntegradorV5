from flask import Flask, render_template
from controllers import routes

if __name__ == '__main__':
    app = Flask(__name__, template_folder='views')
    routes.init_app(app)
    app.run(host='localhost', port=4100, debug=True)