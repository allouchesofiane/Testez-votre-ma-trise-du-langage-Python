class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library():
    def __init__(self):
        self.books = [] # Livres disponibles
        self.borrow_books = [] # Livres empruntés

    def add_book(self, book):
        # Ajout livre
        self.books.append(book)

    def remove_book(self, book_title):
        #Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument.
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return None
            
    def borrow_book(self, book_title): 
        #Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument. Le livre doit être retiré de la liste des livres disponibles et ajouté dans la liste des livres empruntés.
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                return None
            
    def return_book(self, book_title): 
        #Rend un livre emprunté à la bibliothèque en utilisant le titre du livre comme argument. Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                return None
            
    def available_books(self): 
        #Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque.
        return [book.title for book in self.books]
    
    def borrowed_books(self): 
        #Renvoie une liste contenant les titres des livres empruntés de la bibliothèque.
        return [book.title for book in self.borrow_books]
    
library = Library()
book1 = Book("le petit prince", "Antoine de Saint-Exupéry ", 1943)
library.add_book(book1)
book2 = Book("1984", "George Orwel", 1949)
library.add_book(book2)
book3 = Book("le grand prince", "Saint-Exupéry ", 1944)
library.add_book(book3)
library.remove_book("le grand prince")
library.borrow_book("1984")
print(library.available_books())
print(library.borrowed_books())
library.return_book("1984")
print(library.available_books())
print(library.borrowed_books())
