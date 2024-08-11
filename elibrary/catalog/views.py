from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
import os
import fitz

def extract_cover_image(pdf_path, image_path):
    pdf_document = fitz.open(pdf_path)
    first_page = pdf_document.load_page(0)
    pix = first_page.get_pixmap()
    pix.save(image_path)
    pdf_document.close()

def book_list(request):
    # books = Book.objects.all().order_by('-score')
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        ).order_by('-score')
    else:
        books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/catalog.html', {'books': page_obj, 'paginator': paginator, 'page_obj': page_obj})

@login_required(login_url="/users/login/")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()

            if book.cover_image and book.cover_image.name.endswith('.pdf'):
                pdf_path = book.cover_image.path
                image_path = f'{pdf_path}.png'
                
                extract_cover_image(pdf_path, image_path)
                
                book.cover_image.name = f'{book.cover_image.name}.png'
                book.save()
            
            return redirect('catalog:list')
        else:
            print("Form errors:", form.errors)
            print("Form cleaned_data:", form.cleaned_data)
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required(login_url="/users/login/")
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            pdf_file = request.FILES.get('pdf_file')
            
            if pdf_file:
                # Save the PDF file
                book.pdf_file = pdf_file
                book.save()
                
                # Extract the first page and save it as cover image
                pdf_path = book.pdf_file.path
                cover_image_path = os.path.join('media', 'covers', f'{book.pk}.png')
                extract_first_page_as_image(pdf_path, cover_image_path)
                
                # Update the Book instance with the cover image
                with open(cover_image_path, 'rb') as cover_image_file:
                    book.cover_image.save(f'{book.pk}.png', ContentFile(cover_image_file.read()))
                book.save()
            return redirect('catalog:book_detail', book_id=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book':book})

@login_required(login_url="/users/login/")
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('catalog:list')
    return render(request, 'confirm_delete.html', {'book': book})