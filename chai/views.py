from django.shortcuts import render
from .models import ChaiVarity, Store
from django.http import HttpResponse
from .forms import ChaiVarityForm

def all_chai(request):
    chai = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chai': chai})

def order(request):   
    return HttpResponse("Order Page")

def chai_stores(request):
    stores = None
    form = ChaiVarityForm()

    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varities=chai_variety)
        else:
            form = ChaiVarityFrom()
    return render(request, 'chai/chai_stores.html', {
        'stores': stores,
        'form': form
    })