from flask import Flask, render_template
import mlab
from models.movie import Movie

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
  movies = Movie.objects()
  return render_template('index.html', movies=movies)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=False)
 