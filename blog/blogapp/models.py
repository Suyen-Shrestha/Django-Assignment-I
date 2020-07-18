from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title        
