from flask import jsonify, request
from flask_restx import Resource, Namespace
from models import Book, BookSchema

from setup_db import db

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return BookSchema(many=True).dump(Book.query.all()), 200

    def post(self):
        data = request.json
        with db.session.begin():
            db.session.add(Book(**data))
            db.session.commit()
        return '', 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return BookSchema().dump(Book.query.get(bid)), 200

    def put(self, bid):
        data = request.json
        if id in data:
            data.pop('id')
        with db.session.begin():
            Book.query.filter(Book.id == bid).update(data)
            db.session.commit()
        return '', 204

    def delete(self, bid):
        db.session.delete(Book.query.get(bid))
        db.session.commit()
        return '', 204
