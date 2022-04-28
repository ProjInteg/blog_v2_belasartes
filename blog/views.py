from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def formulario(request):
    return render(request, 'blog/formulario.html', {})

def curso(request):
    return render(request, 'blog/curso.html', {})

# Create your views here.
