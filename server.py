import os
from flask import Flask
from book import db, Book
from form import AddNewBook
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from flask import render_template, redirect, url_for
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()

app = Flask(__name__)
# App secret key used for form submission
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
# Name of the DB created for storing book data
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Apply bootstrap to application
Bootstrap5(app)
# Apply custom Bootstrap theme to app
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'zephyr'

# SQLAlchemy database initialization
db.init_app(app)

# Run this for first time to create table from schema defined
# with app.app_context():
# 	db.create_all()

# GET '/'
@app.route('/')
def home():
	collection = db.session.scalars(db.select(Book).order_by(Book.id)).all()
	return render_template('index.html', collection = collection)

# GET '/add'
@app.route('/add', methods=['GET', 'POST'])
def add_new_book():

	add_new_book_form = AddNewBook()

	if add_new_book_form.validate_on_submit():
		
		author = add_new_book_form.author.data
		book_title = add_new_book_form.title.data
		rating = add_new_book_form.rating.data

		print("Adding the data to database...")
		print(f"Author: {author}\nBook: {book_title}\nRating: {rating}")
		print()
		
		new_entry = Book(title=book_title, author=author, rating=rating)
		db.session.add(new_entry)
		db.session.commit()

		return redirect(url_for('home'))

	return render_template('add.html', form=add_new_book_form, btn_text = "Add")

# GET '/edit/:id'
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):

	book = db.get_or_404(Book, book_id)
	
	edit_form = AddNewBook(obj = book)

	for field in edit_form:
		print(field)

	if edit_form.validate_on_submit():
		
		author = edit_form.author.data
		book_title = edit_form.title.data
		rating = edit_form.rating.data

		print("Adding the data to database...")
		print(f"Author: {author}\nBook: {book_title}\nRating: {rating}")
		print()
		
		book.title = book_title
		book.author = author
		book.rating = rating
		db.session.commit()

		return redirect(url_for('home'))

	return render_template('add.html', form=edit_form, btn_text = "Edit")


# DELETE '/:id'
@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete(book_id):

	book = db.get_or_404(Book, book_id)
	db.session.delete(book)
	db.session.commit()

	return redirect(url_for('home'))



if __name__ == '__main__':
	app.run(debug=True)
