from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Category


def order_create(request):

    category = None
    categories = Category.objects.all()

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                            {'order': order
                            })
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart,
                    'form': form,
                    'category': category,
                    'categories': categories,
                   })