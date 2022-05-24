from django.shortcuts import render
from blog.forms import AssociadoForm


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def curso(request):
    return render(request, 'blog/curso.html', {})


def form_modelform(request):
    if request.method == "GET":
        form = AssociadoForm()
        context = {
            'form': form
        }
        return render(request, 'blog/formulario.html', context=context)
    else:
        form = AssociadoForm(request.POST)
        if form.is_valid():
            associado = form.save()
            form = AssociadoForm()

        context = {
            'form': form
        }
        return render(request, "blog/formulario.html", context=context)
