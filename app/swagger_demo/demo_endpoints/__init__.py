# blueprints/documented_endpoints/entities/__init__.py
from flask import request
from flask_restplus import Namespace, Resource, fields
from app.models import Image
from http import HTTPStatus

namespace = Namespace('images', 'Image Repository')

image_model = namespace.model('Image', {
    'id': fields.Integer(
        readonly=True,
        description='Image identifier'
    ),
    'image_url': fields.String(
        required=True,
        description='image url'
    )
})

image_list_model = namespace.model('ImageList', {
    'images': fields.Nested(
        image_model,
        description='List of entities',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of entities',
    ),
})

response_model = namespace.model('Response', {
    'response': fields.String(
        required=True,
        description='image url'
    ),
})

images = []


@namespace.route('')
class entities(Resource):
    '''Get entities list and create new entities'''

    @namespace.response(200, 'Success')
    @namespace.response(500, 'Internal Server error')
    # @namespace.marshal_list_with(image_list_model)
    def get(self):
        '''List all the image URLs'''
        # images = Image.query.all()
        return {
            'entities': images,
            'total_records': len(images)
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(image_model)
    @namespace.marshal_with(response_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Upload a new Image'''

        newImage = {"id": 1, "image_url": request.json['image_url']}
        images.append(newImage)
        return {"response": "Image added!"}, 201
