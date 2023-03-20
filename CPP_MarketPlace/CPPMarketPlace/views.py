from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPPMarketPlace.models import Product
from CPPMarketPlace.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required

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
    return render(request, 'search_results.html', {'results': results})