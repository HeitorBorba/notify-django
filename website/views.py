from django.shortcuts import render

# Create your views here.

def retomar_index(request):
    return render(request, 'site.html')
