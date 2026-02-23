import os
from flask import Flask
from form import AddNewBook
from dotenv import load_dotenv
from flask import render_template
from flask_bootstrap import Bootstrap5

load_dotenv()

# sample data to show the collections
my_collection = [
{
	"title": "Harry Potter and The Philosopher's Stone",
	"author": "J.K.Rowling",
	"rating": "4.5"
},
{
	"title": "Lord of The Rings",
	"author": "J.R.R. Tolkier",
	"rating": "4"
},
{
	"title": "A Game of Thrones",
	"author": "George R.R. Martin",
	"rating": "3.8"
}]

app = Flask(__name__)
# App secret key used for form submission
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
# Apply bootstrap to application
Bootstrap5(app)
# Apply custom Bootstrap theme to app
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'zephyr'

# GET '/'
@app.route('/')
def home():
	return render_template('index.html', collection = my_collection)

# GET '/add'
@app.route('/add')
def add_new_book():
	add_new_book_form = AddNewBook()
	return render_template('add.html', form=add_new_book_form)



if __name__ == '__main__':
	app.run(debug=True)
