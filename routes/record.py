from ..models import Product, db
from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
from pathlib import Path
import json, re
product = Blueprint('products', __name__)