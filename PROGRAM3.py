# Initialize library data
book_ids = [101, 102, 103, 104, 105]
book_names = [
    "Python Programming",
    "Data Structures",
    "Java Basics",
    "Database Systems",
    "Computer Networks"
]

# Input book ID to search
search_id = int(input("Enter Book ID to search: "))

# Linear Search
found = False

for i in range(len(book_ids)):
    if book_ids[i] == search_id:
        print("Book Found!")
        print("Book ID:", book_ids[i])
        print("Book Name:", book_names[i])
        found = True
        break

if not found:
    print("Book not found!")