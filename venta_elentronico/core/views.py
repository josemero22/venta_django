from django.shortcuts import render , HttpResponse

# Create your views here.
def home (request):
    return render(request, 'core/inde.html')
def about (request):
    return render(request, 'core/nosotros.html')
   
def contact  (request):
    return render(request, 'core/contacto.html')

def portfolio (request):
    return render(request, 'core/anuncios.html')

def plantilla (request):
    return render(request, 'core/plantilla.html')
