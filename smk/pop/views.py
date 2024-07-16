from django.shortcuts import render
from .models import Music
# Create your views here.
def index_show(request):
    music = Music.objects.all()

    return render(request,'pop/index.html', {'music':music})

def detail_show(request,pk):
    music = Music.objects.get(id = pk)

    return render(request, 'pop/detail.html',{'music':music})