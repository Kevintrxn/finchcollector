from django.shortcuts import render

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
    all_finches = list(db_finches) + finches
    return render(request, 'finches/index.html', {'finches': all_finches})

