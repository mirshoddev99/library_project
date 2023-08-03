from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.title
