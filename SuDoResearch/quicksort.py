import re
from typing import Iterable, List
from pathlib import Path

home = str(Path.home())


def book_list_parser() -> Iterable[str]:
    # read input
    with open("{}/Desktop/quicksort.txt".format(home), 'r', encoding='utf-8') as f:
        book_list = f.readlines()
        total_books = int(book_list[0])

        # validate total number of books
        if total_books > 100:
            print("Books must be less than 100. ")
            return

        elif total_books < 1:
            print("Invalid number of books.")
            return

        # validate length of booklist
        elif total_books != len(book_list) - 1:
            print("Number on line 1 and length of book list do not tally. ")
            return

        else:
            # parse book string
            for book in book_list[1:]:
                # regex to validate strings in book_list and extract key elements.
                parser = re.search("([a-zA-Z \.]{1,30}), ([a-z A-Z]{1,100}) \(([0-9]{4})\)", book)

                author = parser.group(1)
                title = parser.group(2)
                year = parser.group(3)
                book = book.replace("\n", "")

                yield book, author, title, year


SORT_ORDER = "XOBCDAFGHUJKLMNIPQRSTEVWYZ ."
data = list(book_list_parser())


def custom_alphabet_index(word: str) -> List:
    "Return word as list of indices in custom alphabet."
    return [SORT_ORDER.index(c.upper()) for c in word]


def quicksort(arr: List):
    result = sorted(arr, key=lambda x: (custom_alphabet_index(x[1]),
                                        x[3],
                                        custom_alphabet_index(x[2])))

    for item in result:
        print(item[0])


if __name__ == "__main__":
    quicksort(data)
