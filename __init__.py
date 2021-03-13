from Flask import *
import sqlite3

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
  render_template('index.html')

if __name__ == '__main__':
  app.run()
