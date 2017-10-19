from flask import Blueprint

api_1 = Blueprint('api_1', __name__)

from .user import views
from .main import views
from .blog import views