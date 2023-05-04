from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from CPPMarketPlace.models import Product, UserProfile
from CPPMarketPlace.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from register import views as register
from chat.forms import ChatForm
from chat.models import Thread
from chat import views as chat
#from serializers import ProductSerializer
# Create your views here.

def home(request):
    books = Product.objects.filter(category="Books").exclude(image__exact='').order_by('?')[:4]
    electronics = Product.objects.filter(category="Electronics").exclude(image__exact='').order_by('?')[:4]
    supplies = Product.objects.filter(category="Supplies").exclude(image__exact='').order_by('?')[:4]
    clothes = Product.objects.filter(category="Clothes").exclude(image__exact='').order_by('?')[:4]
    categories = {
        'Books': books,
        'Electronics': electronics,
        'Supplies': supplies,
        'Clothes': clothes,
    }
    return render(request, "index.html", {'categories': categories})

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

def products_by_category(request, category_name):
    products = Product.objects.filter(category__icontains=category_name)
    context = {
        'my_data': products,
        'category_name': category_name
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

def account_detail(request, account_id):
    user_profile = get_object_or_404(UserProfile, user_id=account_id)
    results = Product.objects.filter(owner=account_id)
    return render(request, 'user_profile.html', {'user_profile': user_profile, 'results':results})

def account_settings(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        user_profile.first_name = request.POST['first_name']
        user_profile.last_name = request.POST['last_name']
        user_profile.about = request.POST['about']
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.save()
    return render(request, 'account_settings.html', {'user_profile': user_profile})

def chat_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            otheruserid = request.POST.get("name")
            currentuser = request.user
            otheruser = UserProfile.objects.get(id=otheruserid)
            c = Thread(first_person=currentuser, second_person=otheruser.user)
            c.save()
            return render(request, 'chat/templates/messages.html')
        else:
            return chat.messages_page(request)
    else:
        return register.loginPage(request)
    