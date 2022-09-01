from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('15_3', 'News related endpoints')

news_model = namespace.model('News', {
    'message': fields.String(
        readonly=True,
        description='News message'
    )
})

news_example = {'message': 'News'}

@namespace.route('')
class HelloWorld(Resource):

    @namespace.marshal_list_with(news_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Hello world message endpoint'''

        return news_example