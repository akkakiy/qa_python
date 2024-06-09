# Проект четвертого спринта курса "Инженер по тестированию: от новичка до автоматизатора" 

## Тема "Юнит - Тестирование"

### Содержание:
    conftest.py  -  вспомогательные функции
    main.py      -  тестируемый класс BookCollector
    tests.py     -  методы для тестирования класса BookCollector


## Набор тестовых методов
- test_add_new_book_add_three_books  -  проверка добавления книг (присутствовал изначально)
- test_add_new_book_add_incorrect_name_book  -  проверка на добавление книг с некорректным названием 
- test_add_new_book_add_same_name_book  -  проверка на добавление уже имеющейся книги
- test_set_book_genre_add_genre_in_list  -  проверка на добавление книге жанра из списка 'genre' 
- test_set_book_genre_change_genre_in_list  -  проверка на изменение жанра из списка 'genre'
- test_get_books_with_specific_genre  -  проверка на вывод книги с определенным жанром
- test_get_books_genre_by_name - проверка на вывод жанра книги по названию
- test_get_books_with_specific_genre_not_exist  -  проверка на вывод книги с жанром отсутствующим в списке 'genre'
- test_get_books_for_children  -  проверка на вывод книг для детей
- test_add_book_in_favorites  -  проверка на добавление книги в избранное
- test_delete_book_from_favorites  -  проверка на удаление книги из избранного
- test_delete_book_not_in_favorites  -  проверка на удаление отсутствующей книги в избранном

### Команда для запуска тестов 
`pytest -v tests.py`
### Команда для оценки покрытия
`pytest --cov=main`
