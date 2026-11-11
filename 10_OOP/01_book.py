# Book
class Book:

    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b1 = Book("One Piece","Oda",1200)
print(b1.title)
print(b1.author)
print(b1.pages)