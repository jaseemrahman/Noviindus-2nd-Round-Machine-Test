#Import from the core django
from django.shortcuts import render
from django import forms
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect
#Import from local app/library
from mptt.forms import TreeNodeChoiceField
from datetime import datetime
#Import from local app/library
from tree.models import Book


def tree(request):
    books=Book.objects.all()
    context = {'books':books,"today":datetime.today() }  
    # print(books)  
    return render(request, 'book/tree.html',context)  

def table_view(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request, 'book/table.html',context) 

def last_child(request):
    print(request.POST)
    direction=request.POST['direction']
    book_id=request.POST['book']
    book = Book.objects.get(pk=int(book_id))
    if direction =="left":
        children = book.get_descendants().filter(position=0)
        print(children)

    else:
        children = book.get_descendants().filter(position=1)
    last_child=[]
    if children:
        last_child = list(children)[-1]
    print(last_child)
    books=Book.objects.all() 
    context={"last_child":last_child,'direction':direction,'books':books}
    return render(request, 'book/last.html',context) 
    
   


 
  

