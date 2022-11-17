from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-mega.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.String(250), nullable=False)

        def __repr__(self):
            return '<books %r>' % self.title

    db.create_all()

    #create

    # new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.query(Book).delete()
    # db.session.add(new_book)
    # db.session.commit()

    #read

    # book = Book.query.filter_by(title="Harry Potter").first()

    #update

    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()

    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()

    #delete

    # book_id = 1
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method=="POST":
        new_book= Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect (url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)