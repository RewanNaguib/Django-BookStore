import uuid
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"

    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True) 

    def __str__(self):

        return self.name



class Isbn(models.Model):
    author_title= models.CharField(null="True",blank="True",max_length=50)
    isbn= models.UUIDField(default = uuid.uuid4,editable = False)

    def __str__ (self):
        return f"Author Title:{self.author_title} | Isbn={self.isbn}"






class Note(models.Model):
    note_summary=models.CharField(max_length=1000)

    def __str__ (self):
        return self.note_summary



class Booklet(models.Model):
    title=models.CharField(max_length=255,null="True",blank="True")
    content=models.TextField(max_length=2048)

    categories=models.ManyToManyField(Category)
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="booklets")
    isbn=models.OneToOneField(Isbn,on_delete=models.CASCADE,null=True,blank=True)
    note_summary=models.ForeignKey(Note,null="True",blank="True",on_delete=models.CASCADE)

    def __str__(self):

        return self.title






     

