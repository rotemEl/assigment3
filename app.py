# Imports
from flask import Flask, render_template, request, redirect, flash, url_for, session


# App
app = Flask(__name__)
app.secret_key = '123'


# Data
users = {
    'user1': {
        'Name': 'Tinky Winky', 
        'Email': 't@gmail.com'
    },
    'user2': {
        'Name': 'Dipsy',
        'Email': 'd@gmail.com'
    },
    'user3': {
        'Name': 'Laa-Laa', 
        'Email': 'l@gmail.com'
    },
    'user4': {
        'Name': 'Po',
        'Email': 'p@gmail.com'
    },
    'user5': {
        'Name': 'rotem', 
        'Email': 'r@gmail.com'
     }
}

hobbies = ('reading books', 'singing', 'baking')

# Routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('Home_Page.html', username=session.get('username'))


@app.route('/contact')
def contact():
    return render_template('Contact_Us.html', username=session.get('username'))
  

@app.route('/assignment3_1')
def assignment3_1():
    return render_template('assignment3_1.html', username=session.get('username'),  firstName='Rotem', lastName='Elmalem',
                           hobbies=hobbies)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    if request.method == 'POST':
        if request.form['password'] != 'secret':
            return render_template('assignment3_2.html', username=session.get('username'), search_results=[])
        else:
            session['username'] = request.form['username']
            flash('Logged-in, Tinky Winky')
            return redirect(url_for('assignment3_2'))
    if request.method == 'GET':
        return render_template('assignment3_2.html', username=session.get('username'), search_results=[])


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_results = []
    search_term = request.form['search']
    if search_term == '':
        search_results = users
    else:
        search_results = {'user1': users['user1']}
    return render_template('assignment3_2.html', username=session.get('username'), search_results=search_results)
 

@app.route('/log_out')
def logout_func():
    session['username'] = None
    return render_template('assignment3_2.html', username=session.get('username'), search_results=[])


# Sections
if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)