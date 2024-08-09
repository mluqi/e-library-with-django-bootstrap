from django.db import models

# Create your models here.

class Book(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('reading', 'Reading'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    year = models.DateField()
    score = models.DecimalField(max_digits=3, decimal_places=1)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
