scripture = 0
chapter = 1
book = 2

largest_chapter = 0
largest_bom_chapter = 0
book_largest_chapter = ""
largest_bom = ""

with open("books_and_chapters.txt") as books_file:
    print()
    for line in books_file:
        book_detail = line.strip() 
        line_info = book_detail.split(":")
        if line_info[book]=="Book of Mormon":
           print(f"Scripture: {line_info[scripture]}, Book: {line_info[book]}, Chapters: {line_info[chapter]}")
           if int(line_info[chapter]) > largest_bom_chapter:
                largest_bom_chapter = int(line_info[chapter])
                largest_bom = line_info[scripture]
                

        if int(line_info[chapter]) > largest_chapter:
            largest_chapter = int(line_info[chapter])
            book_largest_chapter = line_info[book]

print()
print(f"Largest BOM: {largest_bom}")
print()
print(f"Largest Book \"{book_largest_chapter}\" has {largest_chapter} chapters ")
print()