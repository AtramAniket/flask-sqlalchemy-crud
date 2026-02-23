from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class AddNewBook(FlaskForm):

	book_name = StringField('Book Name', validators=[DataRequired('Book Name is required')])
	author = StringField('Book Author', validators=[DataRequired('Book AUthor is required')])
	rating = StringField('Rating', validators=[DataRequired('Rating is required')])
	submit = SubmitField('Add Book')
