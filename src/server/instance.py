from flask import Flask
from flask_restplus import Api, Resource, fields


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='API Product',
                       description='API CRUD.',
                       doc='/docs'
                       )

    def run(self):
        self.app.run(
            debug=True,
        )


server = Server()
