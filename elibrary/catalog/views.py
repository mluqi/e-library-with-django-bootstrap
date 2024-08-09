from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book
# # Create your views here.
# def catalogBooks(request):
#     return render(request, 'catalog/catalog.html')
def book_list(request):
    # books = Book.objects.all().order_by('-score')
    books = Book.objects.all()
    paginator = Paginator(books, 8)  # 8 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/catalog.html', {'books': page_obj, 'paginator': paginator, 'page_obj': page_obj})
