from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
  return("<b>This Flask application is Hosted by Nagesh kanade For testing Purpose!</b>")

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':

 app.run()