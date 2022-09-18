from flask import Flask
from flask_restx import Api
from config import Config
from views.books import book_ns
from views.reviews import review_ns
from setup_db import db
from models import Book, Review

app = Flask(__name__)
config = Config()
app.config.from_object(config)
db.init_app(app)

api = Api(app)
api.add_namespace(book_ns)
api.add_namespace(review_ns)

with app.app_context():
    db.create_all()
    b1 = Book(name='Гарри Поттер и Тайная Комната', author='Джоан Роулинг', year=1990, pages=400)
    b2 = Book(name='Граф Монте-Кристо', author='Дюма', year=1510, pages=1344)
    b3 = Book(name='Гарри Поттер и Орден Феникса', author='Джоан Роулинг', year=1993, pages=500)
    b4 = Book(name='Гарри Поттер и Кубок Огня', author='Джоан Роулинг', year=1994, pages=600)

    a1 = Review(user='Oleg', rating=5, book_id=1)
    a2 = Review(user='Ivan', rating=6, book_id=2)
    a3 = Review(user='John', rating=4, book_id=3)
    a4 = Review(user='Diana', rating=3, book_id=4)
    with db.session.begin():
        db.session.add_all([b1, b2, b3, b4])
        db.session.add_all([a1, a2, a3, a4])
        db.session.commit()

if __name__ == '__main__':
    app.run()
