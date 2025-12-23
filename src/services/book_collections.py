from typing import List, Iterable, Any

from src.services.book import Book


class BookCollection:
    def __init__(self, books: Iterable[Book] | None = None):
        if books is None:
            books = ()
        elif any(not isinstance(book, Book) for book in books):
            raise TypeError("Book elements expected")
        self.__items: List[Book] = list(books)

    def __getitem__(self, key: int | slice):
        return self.__items[key]

    def __iter__(self):
        return iter(self.__items)

    def __len__(self):
        return len(self.__items)

    def __contains__(self, item: Any):
        return item in self.__items

    def append(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.append(item)

    def remove(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Book object expected, {type(item)} given")
        self.__items.remove(item)

    def __delitem__(self, key: int | slice):
        del self.__items[key]

    def __str__(self) -> str:
        return str([str(book) for book in self.__items])

    def __add__(self, other: BookCollection) -> BookCollection:
        if not isinstance(other, BookCollection):
            raise TypeError(f"cannot add BookCollection with {type(other)}")
        return BookCollection(self.__items + other.__items)

    def __iadd__(self, other: BookCollection) -> BookCollection:
        if not isinstance(other, BookCollection):
            raise TypeError(f"cannot add {type(other)} to BookCollection")
        self.__items.extend(other.__items)
        return self
