from django.shortcuts import render

from .models import Category, Product


def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'core/categories_list.html', context)


def products_list(request, id):
    products = Product.objects.filter(categories=id)
    category = Category.objects.get(id=id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'core/products_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    images = product.itemimage_set.all()
    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'core/product_detail.html', context)
