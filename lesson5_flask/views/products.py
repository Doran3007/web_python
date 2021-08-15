from werkzeug.exceptions import BadRequest
from flask import Blueprint, render_template

products_app = Blueprint('products_app', __name__)

PRODUCTS = {
    1: 'BMW',
    2: 'Marsedes-benz',
    3: 'Jaguar',
    4: 'Toyota',
    5: 'Ford',
}


@products_app.route('/')
def products_page():
    return render_template('products/products_page.html', products=PRODUCTS)


@products_app.route('/<int:product_id>/', endpoint='products_detail')
def product(product_id: int):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise BadRequest(f"invalid product id #{product_id}")
    return render_template("products/products_detail.html", product_id=product_id, product_name=product_name)