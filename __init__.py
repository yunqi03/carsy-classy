from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  data=[("Benz",'1'),('Merc','2')]
  return render_template('Show_data.html', data=data)

if __name__ == '__main__':
  app.run()
