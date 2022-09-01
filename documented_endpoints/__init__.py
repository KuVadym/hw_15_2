from flask import Blueprint
# import flask.scaffold
# flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api
from .news import namespace as news_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)

api_extension.add_namespace(news_ns)
