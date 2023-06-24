from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand, Gallery
from django.contrib import messages
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger 


def index(request):
    category = None
    categories = Category.objects.all()

    products = Product.objects.filter(available=True)

    top = Product.objects.filter(top=1)


    return render(request, 'shop/index.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'top': top,

    })

def product_list(request, category_slug=None):

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

    category = None
    categories = Category.objects.all()
    
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all()
    
    paginator = Paginator(products, 6)    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        pass

    return render (request, 'shop/product/list.html', context={
        'category': category,
        'categories': categories,
        'products': products,
        'brand': brand,
        'page': page,

    })



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    images = Gallery.objects.filter(product=product)
    return render(request, 'shop/product/detail.html', context={
                                                        'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'images': images,
    })



def search_product(request):

    brand = Brand.objects.all()
    brandID = request.GET.get('brand') 

    category = None
    categories = Category.objects.all()

    if brandID:
        products = Product.objects.filter(brand = brandID)
    else:
        Product.objects.all() 
        
    query = request.GET.get("Q")
    products = Product.objects.filter(name__icontains=query)


    

    return render(request, 'shop/product/search.html', context={'products': products,
                                                                'query': query,
                                                                'category': category,
                                                                'categories': categories,
                                                                'brand': brand,                                                            
                                                                })


