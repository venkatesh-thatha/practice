from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import user
from application.variables import CUSTOMER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        address = request.form['address']
        role = request.form['role']
        
        # Create a new User object
        new_user = User(name=name, username=username, email=email, phone=phone,
                        password=password, address=address, role=CUSTOMER)
        
        # Add the new user to the database session
        db.session.add(new_user)
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect to the login page
        return redirect(url_for('login'))
    
    # If the request method is GET, render the register.html template
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Query the database for the user with the provided username
        user = User.query.filter_by(username=username).first()
        
        # If a user with the provided username exists and the password matches, redirect to the index page
        if user and user.password == password:
            return redirect(url_for('index'))
    
    # If the request method is GET or if authentication fails, render the login.html template
    return render_template('login.html')
