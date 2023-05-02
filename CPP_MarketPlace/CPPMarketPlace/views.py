from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPPMarketPlace.models import Product, UserProfile
from CPPMarketPlace.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from register import views as register
#from serializers import ProductSerializer
# Create your views here.

def home(request):
    return render(request, "index.html")

def helloWorld(request):
    return HttpResponse('Hello World')

#Shows list of all items in product database
@api_view(['GET'])
def product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#Add item to product database
@api_view(['POST'])
def addItem(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

def products(request):
    products = Product.objects.all()
    context={
      'my_data':products
    }
    return render(request, 'products.html', context)

def search(request):
    productName = request.GET.get('query')
    #Return any product with name that contains query
    results = Product.objects.filter(name__icontains=productName)
    return render(request, 'search_results.html', {'results': results , 'query':productName})

def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                 # create a new product instance with the user as the owner
                product = form.save(commit=False)
                product.owner = user
                product.save()
                print("Added")
                return render(request, 'create_product.html', {'form': form, 'success': True})
            else:
                print("Did not add")
                return render(request, 'create_product.html', {'form': form, 'error_message': 'Product was not added.'})
        else:
            form = ProductForm()
        return render(request, 'create_product.html', {'form': form})
    else:
        return register.loginPage(request)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=product.owner)
    context = {'product': product, 'user_profile': user_profile}
    return render(request, 'product_page.html', context)