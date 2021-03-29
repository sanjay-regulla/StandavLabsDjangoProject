from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import *
from django.views.generic import View
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def user_signup(request):

    form = UserCreationForm()
               

    if request.POST:
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('/login/')
        else :
            return redirect('/signup/')
            
    return render(request,'new_user_sign_up.html',locals()) 

def user_authenticate(request,user_name,password):

    try:
        username = User.objects.get(username=user_name.lower()).username
    except Exception as e:
        username = None
        password = None

    user = authenticate(username=username, password=password)
    
    return user
        
def user_login(request):

    if request.POST:
        user_name = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = user_authenticate(request,user_name,password)
        
        if user and user.is_active:
            login(request, user)
            return redirect('/product/')
        else:
            error_msg = "Your User ID & Password Combination is Incorrect" 
    
        return render(request,'user_login.html',locals())

    return render(request,'user_login.html',locals())




def user_products(request):


    title = 'List of Products'
    if not request.user.is_authenticated:
        return redirect('/login/')
    user_name = User.objects.get(id=request.user.id)
        
    product_li = UserProducts.objects.filter(user_id = user_name).values()
    return render(request,'product_list.html',locals())

def add_user_products(request):

        
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.POST :

        post_data = request.POST
        user_name = User.objects.get(id=request.user.id)
       
        product_li = UserProducts.objects.create(user_id = user_name, product_name =post_data['product_name'])
        return redirect('/product/')

    
    return render(request,'new_user_product.html',locals())        



def user_logout(request):
    
    logout(request)
    return redirect('/login/')