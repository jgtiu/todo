from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewTaskForm
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    tasks = [
        {
            'task_name': 'Build a rocket',
            'due_date': datetime(2020, 6, 23)
        },
        {
            'task_name': 'Fight a mummy',
            'due_date': datetime(2020, 6, 25)
        }
    ]
    return render_template('index.html', title='Home', user=user, tasks=tasks)


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = NewTaskForm()
    if form.validate_on_submit():
        flash('Add task for {} {}'.format(form.task_name.data, form.due_date.data))
        return redirect(url_for('index'))
    return render_template('add_task.html',  title='Enter New Task', form=form)