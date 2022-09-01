from flask import request
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('news', 'News fake endpoints')

news_model = namespace.model('News', {
    'id': fields.Integer(
        readonly=True,
        description='News identifier'
    ),
    'subtitle': fields.String(
        required=True,
        description='News title'
    ),
    'text': fields.String(
        required=True,
        description='News title'
    )
})

news_list_model = namespace.model('NewsList', {
    'id': fields.Integer(
        readonly=True,
        description='News identifier'
    ),
    'title': fields.String(
        required=True,
        description='News title'
    ),
    'link': fields.String(
        required=True,
        description='News title'
    ),
    'news': fields.Nested(
        news_model,
        description='List of news',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of news',
    ),
})

news_example = {'id': 1, 'subtitle': 'News subtitle', 'text':'News text'}

@namespace.route('')
class news_list(Resource):
    '''Get news list'''

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(news_list_model)
    def get(self):
        '''List with all the news'''
        news_list = [news_example]

        return {
            'news': news_list,
            'total_records': len(news_list)
        }


@namespace.route('/<int:news_id>')
class news(Resource):
    '''Read news'''

    @namespace.response(404, 'News not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(news_model)
    def get(self, news_id):
        '''Get news_example information'''

        return news_example