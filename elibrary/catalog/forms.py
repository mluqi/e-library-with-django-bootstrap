from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'category', 'description', 'pages', 'status', 'score', 'cover_image', 'pdf_file']