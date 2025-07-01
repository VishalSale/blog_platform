from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
