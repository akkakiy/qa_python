import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_three_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    @pytest.mark.parametrize('book', ['', 'ЗолушкаЗолушкаЗолушкаЗолушкаЗолушкаЗолушкаЗолушка'])
    def test_add_new_book_add_incorrect_name_book(self, book, collector):
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_same_name_book(self, collector):
        books = ['Война и мир', 'Война и мир']
        for book in books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_genre_in_list(self, collector):
        new_book = 'Война и мир'
        genre = 'Детективы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)
        assert collector.get_book_genre(new_book) == genre

    def test_set_book_genre_change_genre_in_list(self, collector):
        new_book = 'Война и мир'
        genre = 'Детективы'
        genre_new = 'Ужасы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)
        collector.set_book_genre(new_book, genre_new)
        assert collector.get_book_genre(new_book) == genre_new

    def test_get_books_with_specific_genre(self, collector, collection_with_books):
        assert collector.get_books_with_specific_genre('Детективы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_genre_by_name(self, collector, collection_with_books):
        assert collector.get_book_genre('Война миров') == 'Фантастика'

    def test_get_books_with_specific_genre_not_exist(self, collection_with_books):
        assert len(collection_with_books.get_books_with_specific_genre('Триллеры')) == 0

    def test_get_books_for_children(self, collection_with_books):
        children_books = collection_with_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Война миров', 'Золушка', '12 стульев']

    def test_add_book_in_favorites(self, collector):
        new_book = 'Война и мир'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        assert new_book in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        new_book = 'Война и мир'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.delete_book_from_favorites(new_book)
        assert new_book not in collector.get_list_of_favorites_books()

    def test_delete_book_not_in_favorites(self, collector):
        one_book = 'SQL Быстрое погружение'
        two_book = 'Война и мир'
        collector.add_new_book(one_book)
        collector.add_book_in_favorites(one_book)
        collector.delete_book_from_favorites(two_book)
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1