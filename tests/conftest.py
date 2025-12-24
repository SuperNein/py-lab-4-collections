import pytest
from src.services.book import Book, DigitalBook, Magazine

@pytest.fixture
def book():
    return Book(
        "title",
        "author",
        2025,
        "genre",
        "12345",
    )

@pytest.fixture
def digital_book():
    return DigitalBook(
        "title",
        "author",
        2025,
        "genre",
        "12345",
    )

@pytest.fixture
def magazine():
    return Magazine(
        "title",
        "author",
        2025,
        "genre",
        "12345",
        issue=5
    )
