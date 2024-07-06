from django.shortcuts import render

# Create your views here.
def home(request):
  # return HttpResponse("<h1>This is our Home Page</h1>")
  return render(request, 'myapp/welcome.html')
