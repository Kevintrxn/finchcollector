from django.shortcuts import render
from .models import Finch
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

finches = [
    {'name': 'Finchious', 'description': 'A smol bird', 'age': 1},
    {'name': 'Ferb', 'description': 'A chonky bird', 'age': 2},
    {'name': 'Ferry', 'description': 'A platapus-looking bird', 'age': 3},
]

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    db_finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': db_finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class finchesList(ListView):
    model = Finch
    template_name = 'finches/index.html'
    context_object_name = 'finches'

class finchesCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class finchesUpdate(UpdateView):
    model = Finch
    fields = ['name', 'description', 'age']
    success_url = '/finches/'

class finchesDelete(DeleteView):
    model = Finch
    success_url = '/finches/'