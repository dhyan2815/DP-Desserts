from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from app.models import Order, MenuItem

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def menu(request):
    # Fetch all menu items
    menu_items = MenuItem.objects.all()
    # Create paginator with 9 items per page
    paginator = Paginator(menu_items, 9)
    
    # Get the current page number from the request
    page_number = request.GET.get('page', 1)

    # Get the items for the current page
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,  # Pass the paginator object to the template
    }
    return render(request, "menu.html", context)

def order(request):
    menu_items = MenuItem.objects.all()

    if request.method == "POST": 
        items = request.POST.getlist('item')  # Get all selected items as a list
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Create a single Order instance
        order = Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            message=message,
            date=datetime.today()
        )

        # Add selected items to the order
        for item_name in items:
            menu_item = MenuItem.objects.get(name=item_name)  # Find the MenuItem by name
            order.items.add(menu_item)  # Add the MenuItem to the Order

        # Save the order and store in the session
        request.session['order_data'] = {
            'items': items,  # Pass the item names for display
            'name' : name,
            'email': email,
            'phone': phone,
            'address': address,
            'message': message,
        }

        return redirect('order_confirmation')

    return render(request, "order.html", {'menu_items': menu_items})

def order_confirmation(request):
    # Retrieve order data from the session
    order_data = request.session.get('order_data', {})
    return render(request, "order_confirmation.html", {'order_data': order_data})   