from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
  return("<b>This Flask application is Hosted by Nagesh kanade For testing Purpose!</b>")

@app.route('/about')
def about():
  return("Hello i am Nagesh Kanade Enthusiast python Web developer!")

if __name__ == '__main__':

 app.run()