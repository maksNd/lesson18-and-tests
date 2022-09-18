# текст задания находится в файле app.py
from setup_db import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    author = Column(String(255))
    year = Column(Integer)
    pages = Column(Integer)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    rating = Column(Integer)
    book_id = Column(Integer)


class BookSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    author = fields.Str()
    year = fields.Integer()
    pages = fields.Integer()


class ReviewSchema(Schema):
    id = fields.Integer()
    user = fields.Str()
    rating = fields.Integer()
    book_id = fields.Integer()
