from flask import Flask, render_template
from application.database import db 

app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.config['SECRET_KEY']='031001'
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 