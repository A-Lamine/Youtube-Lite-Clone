from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Video

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.py')

@main.route('/ydays')
def ydays():
    data = Video.query.all()
    return render_template('ydays.py',video = data)

@main.route('/test')
def test():
    data = Video.query.all()
    return render_template('test.py', video = data)


#Movies Manage


@main.route('/movie')
@login_required
def movie():
    all_data = Video.query.all()
 
    return render_template("movies.py", movies = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@main.route('/insert', methods = ['POST'])
@login_required
def insert():
 
    if request.method == 'POST':
 
        lien = request.form['url']
        title = request.form['title']
 
        my_data = Video(url=lien, title=title)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Movie Inserted Successfully")
 
        return redirect(url_for('main.movie'))
 
 
#this is our update route where we are going to update our employee
@main.route('/update', methods = ['GET', 'POST'])
@login_required
def update():
 
    if request.method == 'POST':
        my_data = Video.query.get(request.form.get('id'))
 
        my_data.url = request.form['url']
        my_data.title = request.form['title']

 
        db.session.commit()
        flash("Movie Updated Successfully")
 
        return redirect(url_for('main.movie'))
 
 
 
 
#This route is for deleting our employee
@main.route('/delete/<id>/', methods = ['GET', 'POST'])
@login_required
def delete(id):
    my_data = Video.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Movie Deleted Successfully")
 
    return redirect(url_for('main.movie'))
