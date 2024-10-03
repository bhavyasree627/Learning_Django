from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages 


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



def add_plant(request):
    if request.method == "POST":
        data = request.POST
        plant_name = data.get('plant_name')
        scientific_name = data.get('scientific_name')
        price = int(data.get('price'))
        age = int(data.get('age'))
        pic = request.FILES.get("pic")
        imported = data.get('imported') == 'on'

        # Create a new plant record
        Plant.objects.create(
            plant_name=plant_name,
            scientific_name=scientific_name,
            price=price,
            age=age,
            pic=pic,
            imported=imported
        )

        # Display success toast message
        messages.success(request, "Plant added successfully!")

    return render(request, 'add_plant.html')


def all_plants(request):
    plants = Plant.objects.all()
    return render(request, 'all_plants.html', {'plants': plants})

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    plant.delete()
    messages.success(request, "Plant deleted successfully!")
    return redirect('all_plants')


def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == "POST":
        data = request.POST
        plant.plant_name = data.get('plant_name')
        plant.scientific_name = data.get('scientific_name')
        plant.price = int(data.get('price'))
        plant.age = int(data.get('age'))
        plant.pic = request.FILES.get('pic') if request.FILES.get('pic') else plant.pic
        plant.imported = data.get('imported') == 'on'
        plant.save()

        messages.success(request, "Plant updated successfully!")
        return redirect('all_plants')

    return render(request, 'update_plant.html', {'plant': plant})