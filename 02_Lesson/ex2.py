from book import Book

library = [Book('Война и мир', 'Толстой Л.'), Book('Гордость и предубеждение', 'Джейн Остин'), Book('Облачный атлас','Дэвид митчел')]

for book in library:
    print(f'{book.title} - {book.author}')