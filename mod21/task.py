# -*- coding: utf-8 -*-
import csv
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, date, timedelta
from sqlalchemy.exc import NoResultFound

engine = create_engine('sqlite:///hw.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
app = Flask(__name__)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)

    author = relationship('Author', backref=backref('books', cascade='all, ' 'delete-orphan', lazy='select'))
    students = relationship('ReceivingBook', back_populates='book')

    def __repr__(self):
        return f'Книга {self.name}, в количестве {self.count}.\nДата выпуска: {self.release_date}.'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    def __repr__(self):
        return f'Автор {self.name} {self.surname}'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(11), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    books = relationship('ReceivingBook', back_populates='student')

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
        return session.query(Student).filter(Student.scholarship is True).all()

    @classmethod
    def get_students_with_higher_score(cls, score):
        return session.query(Student).filter(Student.average_score > score).all()


class ReceivingBook(Base):
    __tablename__ = 'receiving_book'

    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    date_of_issue = Column(DateTime, default=datetime.now)
    date_of_return = Column(DateTime)

    student = relationship('Student', back_populates='books')
    book = relationship('Book', back_populates='students')

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
    books_db = session.query(Book).all()
    books = []
    for book in books_db:
        books.append(book.to_json())
    return jsonify(books=books), 200


@app.route('/debtors')
def get_debtors():
    debtors_bd = session.query(ReceivingBook).filter(ReceivingBook.date_of_return == None).all()
    debtors = []
    for debtor in debtors_bd:
        if debtor.count_date_with_book > 14:
            debtors.append(debtor.to_json())
    return jsonify(debtors=debtors), 200


@app.route('/issue_book', methods=['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    new_issue = ReceivingBook(book_id=book_id,
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
        returned_book = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id,
                                                            ReceivingBook.student_id == student_id).one()
        returned_book.date_of_return = datetime.now()
        session.commit()
        return f'Книга с id {book_id} была возвращена читателем с id {student_id}.'
    except NoResultFound:
        return 'Такой связки book_id и student_id не существует.'


@app.route('/books/author/<int:author_id>/')
def books_by_author(author_id):
    counter = 0
    books = session.query(Book).filter(Book.author_id == author_id).all()
    for book in books:
        book = book.to_json()
        rec_lib = list(session.query(ReceivingBook).filter(ReceivingBook.date_of_return is not None,
                                                           ReceivingBook.book_id == book['id']))
        counter += book['count'] - len(rec_lib)
    return f'Количество оставшихся в библиотеке книг автора с id = {author_id} равно {counter}'


@app.route('/books/did_not_read/<int:student_id>/')
def recommend_books_for_student(student_id):
    books_id = session.query(ReceivingBook.book_id).distinct().filter(ReceivingBook.book_id == Book.id,
                                                                      ReceivingBook.student_id == student_id).all()
    books_id = [book[0] for book in books_id]
    authors_id = session.query(Book.author_id).distinct().filter(ReceivingBook.book_id == Book.id,
                                                                 ReceivingBook.student_id == student_id).all()
    authors_id = [author[0] for author in authors_id]
    books_by_authors = session.query(Book).distinct().filter(Book.author_id.in_(authors_id),
                                                             Book.id.notin_(books_id)).all()
    books = []
    for book in books_by_authors:
        book = book.to_json()
        books.append(book['name'])
    return f'После анализа книг, которые вы уже брали, предлагаем вам почитать эти книги: ' \
           f'{"<br>".join(books) if len(books) != 1 else books[0]}'


@app.route('/books/avr')
def avr_books_amount():
    month = datetime.now().month
    books = session.query(func.count(ReceivingBook.book_id)).filter(ReceivingBook.date_of_issue >= month).scalar()
    students = session.query(func.count(Student.id)).scalar()
    return f'Среднее количество книг, которые студенты брали в этом месяце {round(books / students, 4)}'


@app.route('/books/most_popular/')
def most_popular_book_4():
    book_id = session.query(
        func.count(ReceivingBook.book_id)).filter(ReceivingBook.student_id == Student.id, Student.average_score >= 4.0). \
        group_by(ReceivingBook.book_id).order_by(func.count(ReceivingBook.book_id).desc()).limit(1).one()
    book = session.query(Book).filter(Book.id == book_id[0]).one()
    book = book.to_json()
    return f'Самая популярная книга среди студентов, у которых средний балл больше 4.0: {book["name"]}'


@app.route('/top_10_readers/')
def get_top_10_readers():
    today = datetime.now()
    start_of_year = datetime(today.year, 1, 1)
    end_of_year = datetime(today.year + 1, 1, 1) - timedelta(days=1)
    top_10_students = session.query(Student.name). \
        filter(ReceivingBook.student_id == Student.id, ReceivingBook.date_of_issue > start_of_year,
               ReceivingBook.date_of_issue < end_of_year) \
        .group_by(Student.id). \
        order_by(func.count(ReceivingBook.book_id).desc()).limit(10).all()
    result = ''
    for student in top_10_students:
        result += student[0] + ', '
    return f'ТОП-10 самых читающих студентов в этом году: {result[:-2]}'

@app.route('/students/upload', methods=['POST'])
def upload_students():
    students_file = request.files.get('students_file')
    if not students_file:
        return 'Файл "students_file" не найден', 400
    try:
        students_file.save('students.csv')
        students_list = []
        with open('students.csv', 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for student in reader:
                student['scholarship'] = True if student['scholarship'].lower() == 'true' else False
                students_list.append(student)
        session.bulk_insert_mappings(Student, students_list)
    except Exception as e:
        print(e)
        return 'Ошибка при обработке файла "students_file"', 400
    session.commit()
    return 'Студенты из файла "students_file" были успешно добавлены', 200


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    my_books = session.query(Book).filter(Book.author_id == 1).all()
    my_author = session.query(Author).all()[0]
    app.run()
