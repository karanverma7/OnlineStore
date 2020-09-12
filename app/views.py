from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required

def index(request):
    '''Home page'''

    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    context = {
        'products': Product.objects.filter(id__gt=4),
        'products2': Product.objects.filter(id__lt=5),
        'cartSize': len(cart),
    }

    if request.method == 'POST':
        cart.append(int(request.POST['objectId']))
        return redirect('index')

    return render(request, 'index.html', context)


def cartItems(cart):
    '''Get the cart items from the Ids'''

    cartItems = []
    for id in cart:
        cartItems.append(Product.objects.get(id=id))
    return cartItems


def totalPrice(cart):
    '''Calculate and return total price of cart items'''

    Items = cartItems(cart)
    totalPrice = 0
    for item in Items:
        totalPrice += item.price
    return totalPrice


def removeItem(request):
    '''Remove item from cart'''

    cart = request.session['cart']
    request.session.set_expiry(0)


def cart(request):
    '''Cart View'''

    cart = request.session['cart']
    request.session.set_expiry(0)

    if request.method == 'POST':
        obj = int(request.POST['objectId'])
        obj_index = request.session['cart'].index(obj)
        cart.pop(obj_index)
        return redirect('cart')

    context = {
        'cartSize': len(cart),
        'cartItems': cartItems(cart),
        'totalPrice': totalPrice(cart),
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    '''Checkout Page'''

    cart = request.session['cart']
    request.session.set_expiry(0)

    def getItems():
        items = ""
        for item in cartItems(cart):
            items +=  str(item) + ", "
        return items

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        payM = 'Debit Card'
        orderS = True
        items = getItems()
        payD = "Paid"

        order = Order(
            name=name,
            address=address,
            city=city,
            items=items,
            orderStatus=orderS,
            payment_method=payM,
            payment_data=payD
        )
        order.save()
        cart.clear()
        flag = True
        return render(request, 'checkout.html', { 'flag': flag })

    context = {
        'cartSize': len(cart),
        'cartItems': cartItems(cart),
        'totalPrice': totalPrice(cart),
    }
    return render(request, 'checkout.html', context)
