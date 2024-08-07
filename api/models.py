from django.db import models
import uuid






class Book(models.Model):
    book_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.TextField(unique=True, blank=False, editable=True)
    
    
    def __str__(self):
        return self.title
    



class Author(models.Model):
    author_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.TextField(unique=True, blank=False, editable=True)
    books = models.ManyToManyField(Book, blank=False)
 

    
    def __str__(self):
        return self.name







