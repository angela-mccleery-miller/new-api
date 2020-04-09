from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.String(6))
    rating = db.Column(db.String(10))
    genre = db.Column(db.String(20))
    starring = db.Column(db.String(100))

    print("1 It's working")

    def __init__(self, title, year, rating, genre, starring):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre
        self.starring = starring

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'year', 'rating', 'genre', 'starring')
        

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# # Endpoint to create new movie

@app.route("/movie", methods=["POST"])
def add_movie():
    title = request.json['title']
    year = request.json['year']
    rating = request.json['rating']
    genre = request.json['genre']
    starring = request.json['starring']


    new_movie = Movie( title, year, rating, genre, starring)

    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.get(new_movie.id)

    return movie_schema.jsonify(movie)

    print("2 is STILL working")


# @app.route("/movie", methods=["GET"])
# def get_movie():
#     all_movies = Movie.query.all()
#     result = movies_schema.dump(all_movies)
#     return jsonify(result.data)

#     print("3 is even working!")

# @app.route("/movie/<id>", methods=["GET"])
# def movie_detail(id):
#     movie = Movie.query.get(id)
#     return movie_schema.jsonify(movie)

#     print("4 HOLY HELL AWESOME!")

# @app.route("/movie/<id>", methods=["PUT"])
# def movie_update(id):
#     movie = Movie.query.get(id)
#     title = request.json['title']
#     year = request.json['year']
#     rating = request.json['rating']
#     genre = request.json['genre']
#     starring = request.json['starring']

    
    
#     movie.id = id
#     movie.title = title
#     movie.year = year
#     movie.rating = rating
#     movie.genre = genre
#     movie.starring = starring


#     db.session.commit()
#     return movie_schema.jsonify(movie)

#     print("5 ALMOST THERE BABY!")

# @app.route("/movie/<id>", methods=["DELETE"])
# def movie_delete(id):
#     movie = Movie.query.get(id)
#     db.session.delete(movie)
#     db.session.commit()

#     return movie_schema.jsonify(movie)

#     print("6 FAST and PRAY with GRATITUDE!!!")



if __name__ == "__main__":
    app.run(debug=True)