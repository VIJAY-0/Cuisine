from django.shortcuts import render,redirect
from home.models import *
import keys

# Create your views here.home

def home(request):
    # return HttpResponse('Hello')
    return render(request,'index.html')

def place_order_page(request):
    items=Items.objects.all()
    category=Category.objects.all()
    context={'items':items,
             'category':category}
    return render(request,'place_order.html',context)

def profile(request,order=None):

    return render(request,'profile.html')

def reciveOrder(request):
    if request.method=="POST":
        itemslist=request.POST['itemsJSON']
        amount=request.POST['amount']
        print(itemslist)
        user=request.user
        order=Orders(name=user.email,address="empty",items=itemslist,oid='random')
        order.save()
        
        id=order.order_id
        oid=str(id)+'Food.'
        params={   
            'MID':keys.MID,
            'ORDER_ID':oid,
            'TXN_AMOUNT':amount,
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            "CHANNEL_ID":'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000'


        }

        return redirect('Home:home')
    else:
       return  redirect('Home:profile')
    
