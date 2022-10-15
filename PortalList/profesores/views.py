from django.shortcuts import render

# Create your views here.
def ingresarProfesor(request):
    return render(request, 'admin.html')

def seleccionLista(request):
    return render(request, 'admin.html')

def lista(request):
    return render(request, 'admin.html')