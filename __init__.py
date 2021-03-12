from Flask import *

Flask(__name__)

@app.run('/')
def index(arg):
  render_template('index.html')

if __name__ == '__main__':
  app.run()
