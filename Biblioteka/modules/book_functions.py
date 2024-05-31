
import modules.file_functions as ff
def Show_Books():
    books = ff.read_file("books.pkl")

    for book in books:
        print(book)
    input("Jeigu norite nutraukti paspauskite bet ka...")

def show_overdue_books():
    books = ff.read_file("books.pkl")

    books # select books where book return date != None and issue_date < issue_date + timedelta(days=30)