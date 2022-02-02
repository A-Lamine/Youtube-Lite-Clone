from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import Video

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ydays')
@login_required
def ydays():
    data = Video.query.all()
    return render_template('ydays.html',video = data)

@main.route('/test')
def test():
    data = Video.query.all()
    return render_template('test.html', video = data)


@main.route('/profile')
@login_required
def profile():
    return render_template('Profile.html', name=current_user.name)

