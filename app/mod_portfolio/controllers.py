"""Authentication Module Controllers."""
from flask import Blueprint, render_template

mod_portfolio = Blueprint('user', __name__, url_prefix='/')


# Signup method
@mod_portfolio.route('/', methods=['GET'])
def index():
    """Index Page."""
    return render_template('portfolio/index.html')
