from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

# Modelos
from .models import Bookmark
from .forms import BookmarkForm


def bookmark_list(request):
    bookmarks = Bookmark.public.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'marcador/bookmark_list.html', context)

def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    context = {'bookmark': bookmarks, 'owner': user}
    return render(request, 'marcador/bookmark_user.html', context)

# El decorador @login_required se asegura que la vista es sólo accesible a usuarios autenticados.
@login_required
def bookmark_create(request):
    # Comprobamos si la solicitud se realizó a través de POST
    if request.method == 'POST':
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            form.save(owner=request.user)
            return redirect('marcador_bookmark_user', username=request.user.username)
    else:
        form = BookmarkForm()
    # BookmarkForm. create es un valor binario y es usado para determinar si la plantilla se utiliza para crear o editar un marcador
    return render(request, 'marcador/form.html'), {'form': form, 'create': True}
    
@login_required
def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if bookmark.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if requst.method == 'POST':
        form = BookmarkForm(instance=bookmark, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('marcador_bookmark_user', username=request.user.username)
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'marcador/form.html', {'form': form, 'create': False, 'bookmark': bookmark})