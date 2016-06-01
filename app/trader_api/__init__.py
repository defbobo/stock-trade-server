# -*- coding: utf-8 -*-
from flask import Blueprint

apis = Blueprint('apis', __name__)

from . import views
