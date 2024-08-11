from django.db import models

# Create your models here.

class Book(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('reading', 'Reading'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    year = models.DateField()
    category = models.CharField(max_length=100, default='General')
    description = models.TextField(blank=True)
    pages = models.PositiveIntegerField(default=0)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    cover_image = models.ImageField(default='cover_book.png', blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf/', blank=True, null=True)

    def __str__(self):
        return self.title
