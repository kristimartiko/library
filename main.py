class Book:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0

    def display_page(self):
        return self.content[self.last_page]

    def turn_page(self):
        self.last_page += 1

    