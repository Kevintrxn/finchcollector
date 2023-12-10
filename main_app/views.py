from django.shortcuts import render, redirect
from .models import Finch, Feeding, Toy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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
    id_list = finch.toys.all().values_list('id', flat=True)
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 
        'feeding_form': feeding_form, 
        'toys': toys_finch_doesnt_have
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch = Finch.objects.get(id=finch_id)  
        new_feeding.save()
    return redirect('finches_index')

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

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

