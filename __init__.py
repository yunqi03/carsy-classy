from Flask import *

Flask(__name__)

@app.run('/')
def index(arg, methods=["POST", "GET"]):
  render_template('index.html')

if __name__ == '__main__':
  app.run()
