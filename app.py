from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class contact(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String,nullable=False)
  email = db.Column(db.String,nullable=False)

@app.route('/')
def index():
  return redirect(url_for('form'))
@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/form',methods=['POST','GET'])
def form():
  if request.method == 'POST':
    name = request.form['name']
    mail = request.form['mail']
    rs = contact(name=name,email=mail)
    db.session.add(rs)
    db.session.commit()
    return redirect(url_for('form'))
  else:
   return render_template('form.html')

@app.route('/list')
def list():
 return render_template('list.html',st=contact.query.all())

if __name__ == '__main__':

 app.run(debug=True)