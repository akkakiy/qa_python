import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def collection_with_books(collector):
    list_with_books = collector
    books = ['Война миров', 'Гордость и предубеждение и зомби',
             'Что делать, если ваш кот хочет вас убить', 'Золушка', '12 стульев']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        list_with_books.add_new_book(books[i])
    for i in range(5):
        list_with_books.set_book_genre(books[i], genre[i])
    return list_with_books