from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
  return("<b>This Flask application is Hosted by Nagesh kanade For testing Purpose!</b>")

if __name__ == '__main__'

 app.run()