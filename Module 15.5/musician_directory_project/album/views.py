from django.shortcuts import render, redirect
from . import forms
from . models import Album

# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album_form})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        album_form = forms.AlbumForm(request.POST, instance=album) # user er post request data ekhane capture korlam
        if album_form.is_valid(): # post kora data gula amra valid kina check korechi
            album_form.save() # jodi data valid hoi tahole database e save korbo
            return redirect('homepage') # sob thik thakle etake add category ei url e pathiye dibo
    
    return render(request, 'add_album.html', {'form': album_form})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')