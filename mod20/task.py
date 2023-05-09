# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, date
from sqlalchemy.exc import NoResultFound

engine = create_engine('sqlite:///hw.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
app = Flask(__name__)


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Книга {self.name}, в количестве {self.count}.\nДата выпуска: {self.release_date}.'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    def __repr__(self):
        return f'Автор {self.name} {self.surname}'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(11), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'Читатель: {self.name} {self.surname}\n' \
               f'Номер телефона: {self.phone}\n' \
               f'Email: {self.email}\n' \
               f'Средний балл: {self.average_score}\n' \
               f'{"Живет в общежитии." if self.scholarship else "Не живет в общежитии."}'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship is True).all()

    @classmethod
    def get_students_with_higher_score(cls, score):
        return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now() - self.date_of_issue).days


@app.route('/all_books')
def get_books():
    books_db = session.query(Books).all()
    books = []
    for book in books_db:
        books.append(book.to_json())
    return jsonify(books=books), 200


@app.route('/debtors')
def get_debtors():
    debtors_bd = session.query(ReceivingBooks).filter(ReceivingBooks.date_of_return == None).all()
    debtors = []
    for debtor in debtors_bd:
        if debtor.count_date_with_book > 14:
            debtors.append(debtor.to_json())
    return jsonify(debtors=debtors), 200


@app.route('/issue_book', methods=['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    new_issue = ReceivingBooks(book_id=book_id,
                               student_id=student_id,
                               date_of_issue=datetime.now())
    session.add(new_issue)
    session.commit()
    return f'Книга с id {book_id} была выдана читателю с id {student_id}.\n ' \
           f'Дата выдачи выдачи: {date.today()}\n' \
           f'Не забудьте вернуть книгу через 14 дней!'

@app.route('/return_book', methods=['POST'])
def return_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        returned_book = session.query(ReceivingBooks).filter(ReceivingBooks.book_id == book_id,
                                                             ReceivingBooks.student_id == student_id).one()
        returned_book.date_of_return = datetime.now()
        session.commit()
        return f'Книга с id {book_id} была возвращена читателем с id {student_id}.'
    except NoResultFound:
        return 'Такой связки book_id и student_id не существует.'


if __name__ == '__main__':
    app.run()
