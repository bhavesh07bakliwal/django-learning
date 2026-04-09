from django.shortcuts import render
from .models import ChaiVarity
# Create your views here.
def all_chai(request):
    chai = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html', {'chai': chai})
def order(request):   
    return HttpResponse("Order Page ")