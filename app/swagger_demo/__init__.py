# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from app.endpoints.image_repo import namespace as hello_world_ns

blueprint = Blueprint('image_repo', __name__, url_prefix='/demo')

api_extension = Api(
    blueprint,
    title='Dinu\'s Image Repo! ',
    version='1.0',
    description='Save and grab image URLs! Click the image dropdown to see actions. To upload a new image URL, use the Post function. To see existing images, use the get method!',
    doc='/'
)

api_extension.add_namespace(hello_world_ns)
