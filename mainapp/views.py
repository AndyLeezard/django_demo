from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item, Visitor
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return HttpResponse('This is an index HttpResponse. Please enter /mainapp to see the html element.')

def htmlElement(request):
    items = Item.objects.all
    return render(request, "mainapp/index.html", {
        'show_items' : True,
        'items' : items
    })

def item_details(request, item_id):
    try:
        selected_item = Item.objects.get(slug=item_id)
        visitors = Visitor.objects.filter(item=selected_item)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                booker_email, booked_date = registration_form.cleaned_data['email'], registration_form.cleaned_data['date'] # better suited than .save() method here
                booker, _ = Visitor.objects.get_or_create(email=booker_email,date=booked_date) # because this it will avoid duplicates. The low-dash is supposed to be "was_created" but this is not interesting here.
                selected_item.visitors.add(booker)
                return redirect('booking-success', item_id = item_id)
        return render(request, 'mainapp/item-details.html',{
                'status' : True,
                'item' : selected_item,
                'form' : registration_form,
                'visitors' : visitors
        })
    except Exception as exc:
        print(exc)
        return render(request, 'mainapp/item-details.html', {
            'status' : False,
            'item' : {}
        })

def booking_success(request, item_id):
    booked_item = Item.objects.get(slug=item_id)
    return render(request, 'mainapp/booking-success.html', {
        'item': booked_item
    })