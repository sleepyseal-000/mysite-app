from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import To_do, To_cook, To_wish

# Create your views here. (View our webpages)


def homepage(request):
    context= {
        'to_do_items': To_do.objects.all(), 
        'to_cook_items': To_cook.objects.all(),
        'to_wish_items': To_wish.objects.all()
        }
    return render(request,'polls/index.html', context)


#Insert 
def insert_to_do_item(request:HttpRequest):
    todo = To_do(content = request.POST['content'])
    todo.save()
    return redirect('/')

def insert_to_cook_item(request:HttpRequest):
    todo = To_cook(content = request.POST['content'])
    todo.save()
    return redirect('/')

def insert_to_wish_item(request:HttpRequest):
    todo = To_wish(content = request.POST['content'])
    todo.save()
    return redirect('/')

#Delete
def delete_to_do_item(request, to_do_id):
    to_do_delete = To_do.objects.get(id=to_do_id)
    to_do_delete.delete()
    return redirect('/')

def delete_to_cook_item(request, to_cook_id):
    to_cook_delete = To_cook.objects.get(id=to_cook_id)
    to_cook_delete.delete()
    return redirect('/')

def delete_to_wish_item(request, to_wish_id):
    to_wish_delete = To_wish.objects.get(id=to_wish_id)
    to_wish_delete.delete()
    return redirect('/')
