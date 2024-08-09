# import sqlite3
#
# #create a connection to new database
# db = sqlite3.connect("books-collection.db")
#
# ''' cursor is also known as the mouse or pointer.
# If we were working in Excel or Google Sheet,
# we would be using the cursor to add rows of data or edit/delete data,
#  we also need a cursor to modify our SQLite database. '''
#
#
# # create a cursor which will control our database.
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# TODO: create database
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy(model_class=Base)
# initialize the extension
db.init_app(app)


# todo: create table called books
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# todo: create table schema in the database. Requires apllication context
with app.app_context():
    db.create_all()

# todo: create record/enrty
with app.app_context():
    new_book = Book(id=1, title="Freedom", author="OSHO", rating=9.5)
    db.session.add(new_book)
    db.session.commit()