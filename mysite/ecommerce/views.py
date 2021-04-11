from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@csrf_exempt
def home(request):
    context = {}
    context['data'] = Product.objects.all()
    context['category'] = Product_Category.objects.all()

    return render(request, 'crud1.html', context)

@csrf_exempt
def addEmployee(request):
    # import pdb; pdb.set_trace()
    context = {}
    context['data'] = Product.objects.all()

    if request.method == "POST":
        emp_edit_name = request.POST.get('emp_edit_name')
        emp_delete_name = request.POST.get('emp_delete_name') 
        if emp_edit_name:
            prodedit = Product.objects.get(id=emp_edit_name)
            prodedit.name = request.POST.get('product')
            prodedit.color = request.POST.get('color')
            prodedit.brand = request.POST.get('brand')
            prodedit.price = request.POST.get('price')
            prodedit.category = Product_Category.objects.get(id=request.POST.get('category'))
            prodedit.save()

                    
        elif emp_delete_name:
            Product.objects.get(id=emp_delete_name).delete()
            print('deleted')


        else:
            addprod = Product() 
            addprod.name = request.POST.get('name')
            addprod.color = request.POST.get('color')
            addprod.brand = request.POST.get('brand')
            addprod.price = request.POST.get('price')
            addprod.category = Product_Category.objects.get(id=request.POST.get('category'))
            addprod.save()
        
    
    return render(request, 'table1.html', context)
    

    # return JsonResponse({'data':request.POST})

def landing_page(request):
    context = {}
    return render(request, 'landing.html', context)

@csrf_exempt
def search(request):
    context = {}
    import pdb; pdb.set_trace()
    product_searched = Product.objects.filter(Q(name__iexact='test'))

    return render(request, 'landing.html', context)


