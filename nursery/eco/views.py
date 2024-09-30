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









    # return HttpResponse(
    #     """
    #     <h1> Hello Welcome to Nursery</h1>
    #     <h5> See all the available species</h5>
    #     <p>Select your likes from below</p>
    #      """
    # )
    

