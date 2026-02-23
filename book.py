from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Book(db.Model):
	id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
	title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
	author: Mapped[str] = mapped_column(String(255), nullable=False)
	rating: Mapped[int] = mapped_column(Integer, nullable=False)

	def __repr__(self):
		return f'Book {self.title}'