from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def formulario(request):
    return render(request, 'blog/formulario.html', {})

# Create your views here.
