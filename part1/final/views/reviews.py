import requests
from flask import request
from flask_restx import Resource, Namespace
from models import Review, ReviewSchema

from setup_db import db

review_ns = Namespace('reviews')


@review_ns.route('/')
class ReviewsView(Resource):
    def get(self):
        return ReviewSchema(many=True).dump(Review.query.all()), 200

    def post(self):
        data = request.json
        with db.session.begin():
            db.session.add(Review(**data))
            db.session.commit()
        return '', 201


@review_ns.route('/<int:rid>')
class ReviewView(Resource):
    def get(self, rid):
        return ReviewSchema().dump(Review.query.get(rid)), 200

    def put(self, rid):
        data = request.json
        if 'id' in data:
            data.pop('id')
        with db.session.begin():
            Review.query.filter(Review.id == rid).update(request.json)
            db.session.commit()
            return '', 204

    def delete(self, rid):
        with db.session.begin():
            db.session.delete(Review.query.get(rid))
            db.session.commit()
            return '', 204
