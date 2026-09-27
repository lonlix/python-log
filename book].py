class Book:
    def __init__(self, title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.done = False

    def mark_read(self):
        self.done = True
    def __str__(self):
        status = "Выполнено" if self.done else "Не выполнено"
        return f'{status} {self.title} {self.author} Осталось {self.pages} c.'

b = Book("Wsl2", "linux", 700)
print(b)
b.mark_read()
print(b.done)
print(b)


