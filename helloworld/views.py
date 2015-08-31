from django.shortcuts import render
from models import Visitors


def index(request):
    visitors = Visitors.objects.all()

    if not visitors:
        visitors = Visitors.objects.create(total_visitors=0)
    else:
        visitors = visitors[0]

    visitors.total_visitors += 1
    visitors.save()

    return render(request, 'index.html', {'total_visitors': visitors.total_visitors})