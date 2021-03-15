from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  data=[('1',"Benz",'1','OK'),('2','Merc','2','OK')]
  return render_template('Show_data.html', data=data)

if __name__ == '__main__':
  app.run()
