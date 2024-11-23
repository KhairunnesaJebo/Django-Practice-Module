from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.

def home(request):
    return render(request, 'home.html')



def example_form(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, 'django_form.html', {'form': form})
