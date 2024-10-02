from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    plants=[
        {'name':'Rose', 'price': 100},
        {'name':'Lily', 'price': 100},
        {'name':'Crysanthemum', 'price': 100},
        {'name':'Tulip', 'price': 100},
    ]
    message = "Wonder world of Green"
    return render(request, 'home.html',context={"plants":plants,"msg":message})


def contact(request):
    return render(request, 'contact.html')

def nursery(request):
    plants=[
        {'name':'Rose', 'price': 100},
        {'name':'Lily', 'price': 99},
        {'name':'Crysanthemum', 'price': 65},
        {'name':'Tulip', 'price': 100},
        {'name':'Jasmine','price':45}
    ]
    return render(request,'nursery.html', context={"plants":plants})


