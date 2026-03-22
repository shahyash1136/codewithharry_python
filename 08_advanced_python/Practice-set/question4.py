# 4. Magic/Dunder Methods
# 1. Create a class  Book  with attributes  title  and  author .
#     a. Implement  __str__()  so that printing the object displays  "Title by Author" .
#     b. Implement  __len__()  so that  len(book)  returns the length of the title.
# 2. Create two  Book  objects and test these methods.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)
    
b1 = Book("Batman Vs Superman","DC")
b2 = Book("The amazing spiderman", "Marvel")

print(str(b1))
print(len(b1))
print(str(b2))
print(len(b2))