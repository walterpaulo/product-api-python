from flask import Flask
from src.server.instance import server
from flask_restplus import Api, Resource

app, api = server.app, server.api


@api.route('/')
class ProductList(Resource):
    def get(self,):
        return 'Product CRUD - API'
