from django.shortcuts import render
from .models import Countries
from django.shortcuts import render, get_object_or_404

# Create your views here.
# def home(request):
#   # return HttpResponse("<h1>This is our Home Page</h1>")
#   return render(request, 'myapp/welcome.html')


def app(request):
  x = Countries.objects.all()
  return render(request, 'myapp/welcome.html', {'obj': x})

def country_detail(request, country_name):
  obj = get_object_or_404(Countries, name=country_name)
  return render(request, 'myapp/country_detail.html', {'obj': obj})