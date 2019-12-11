from django.shortcuts import render
from .forms import PedidoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')

def cadastro(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'formulario': form
    }
    return render(request, 'cadastro.html', context)