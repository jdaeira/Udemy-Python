mylist = [1, 2, 3]
print(len(mylist))

class Sample():
    pass


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book Object has been deleted")

myBook = Book("Python Rocks", "John", 250)
print(myBook)
print(str(myBook))
print(len(myBook))

del myBook  # deletes the myBook Object