from django.db import models

# author model
class Author(models.Model):
    author_id = models.AutoField(primary_key = True)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    author_contact = models.CharField(max_length=15)

    class Meta:
        db_table = "author"


# book model
class Book(models.Model):
    book_id = models.AutoField(primary_key = True)
    book_name = models.CharField(max_length=100)
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)      
    
    class Meta:
        db_table = "book"


