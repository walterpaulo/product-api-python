from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

product_db = [
    {'id': 0, 'name': 'teclado', 'price': '50.00'},
    {'id': 1, 'name': 'mouse', 'price': '40.00'}
]


@api.route('/products')
class ProductList(Resource):
    def get(self,):
        return product_db

    def post(self, ):
        response = api.payload
        product_db.append(response)
        return response, 200
