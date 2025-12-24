import pytest


def test_book_initialization(book):
    assert book.title == "title"
    assert book.author == "author"
    assert book.year == 2025
    assert book.genre == "genre"
    assert book.isbn == "12345"
    assert book.borrowed == False

def test_digital_book_initialization(digital_book):
    assert digital_book.title == "title"
    assert digital_book.author == "author"
    assert digital_book.year == 2025
    assert digital_book.genre == "genre"
    assert digital_book.isbn == "12345"

def test_magazine_initialization(magazine):
    assert magazine.title == "title"
    assert magazine.author == "author"
    assert magazine.year == 2025
    assert magazine.genre == "genre"
    assert magazine.isbn == "12345"
    assert magazine.borrowed == False
    assert magazine.issue == 5


def test_str_book(book, digital_book, magazine):
    assert str(book) == f"<<12345: author, title, 2025: genre>>"
    assert str(digital_book) == f"<<12345: author, title, 2025: genre>>"
    assert str(magazine) == f"<<12345: author, title, 2025, #5: genre>>"


def test_repr_book(book, digital_book, magazine):
    assert repr(book) == (f"Book"
                f"(title='title', author='author', year=2025, "
                f"genre='genre', isbn='12345', borrowed=False)")
    assert repr(digital_book) == (f"DigitalBook"
                f"(title='title', author='author', year=2025, "
                f"genre='genre', isbn='12345')")
    assert repr(magazine) == (f"Magazine"
                f"(title='title', author='author', year=2025, "
                f"genre='genre', isbn='12345', borrowed=False, issue=5)")
