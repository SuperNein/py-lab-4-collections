class Book:
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
            borrowed: bool = False,
    ):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.borrowed = borrowed

    def __call__(self) -> bool:
        self.borrowed = not self.borrowed
        return self.borrowed

    def __str__(self) -> str:
        return f"<<{self.isbn}: {self.author}, {self.title}, {self.year}>>"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r}, borrowed={self.borrowed!r})")


class DigitalBook(Book):
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
    ):
        super().__init__(title, author, year, genre, isbn)
        self.readers: int = 0

    def __call__(self, readers_num: int = 1) -> int:
        self.readers += readers_num
        return self.readers

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r})")


class Magazine(Book):
    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            genre: str,
            isbn: str,
            borrowed: bool = False,
            issue: int = 0,
    ):
        super().__init__(title, author, year, genre, isbn, borrowed)
        self.issue = issue

    def __str__(self) -> str:
        return super().__str__()[:-2] + (">>" * (not self.issue)) + (f", #{self.issue}>>" * self.issue)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"genre={self.genre!r}, isbn={self.isbn!r}, "
                f"borrowed={self.borrowed!r}, issue={self.issue!r})")


if __name__ == "__main__":
    db = DigitalBook(
        "tittle",
        "author",
        2078,
        "genre",
        "isbn",
    )
    print(repr(db))
    print(str(db))
    print(db())
    print(db(3))

    mag = Magazine(
        "tittle",
        "author",
        2078,
        "genre",
        "isbn",
        issue=1
    )
    print(repr(mag))
    print(str(mag))
    print(mag())
    print(mag())
