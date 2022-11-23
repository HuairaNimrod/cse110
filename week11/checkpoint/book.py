with open("books.txt") as books_file:
    print()
    for book in books_file:
        print(book.strip())
print()