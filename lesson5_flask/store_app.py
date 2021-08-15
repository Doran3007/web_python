from flask import Flask, render_template
from flask.globals import request
from lesson5_flask.views import products_app

store_app = Flask(__name__)
store_app.register_blueprint(products_app, url_prefix='/products')


@store_app.route('/', methods=['GET', 'POST'])
def index():
    name = 'World'
    if request.method == 'POST':
        name = request.form.get('name', 'world')
    return render_template('index.html', name=name)


@store_app.route('/product/<int:product_id>/')
def product(product_id):
    return 'show product_id%r' % product_id
