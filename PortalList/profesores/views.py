from django.shortcuts import render

# Create your views here.
def ingresarProfesor(request):
    if request.method == 'GET':
        return render(request, 'ingresarProfesor.html')

def seleccionLista(request):
    if request.method == 'GET':
        return render(request, 'seleccionLista.html')

def lista(request):
    if request.method == 'GET':
        return render(request, 'lista.html')