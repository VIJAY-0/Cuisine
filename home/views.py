from django.shortcuts import render,redirect
from home.models import *
from home import  keys

# Create your views here.home

def home(request):
    # return HttpResponse('Hello')
    items=Items.objects.all()
    category=Category.objects.all()
    context={'items':items,
             'category':category}
    return render(request,'index.html',context)

def place_order_page(request):
    items=Items.objects.all()
    category=Category.objects.all()
    context={'items':items,
             'category':category}
    return render(request,'place_order.html',context)

def profile(request):
    user=request.user
    placed_order=Orders.objects.filter(name=user.email)
    context={'prev_orders':placed_order}
    return render(request,'profile.html',context)

def reciveOrder(request):
    if request.method=="POST":
        itemslist=request.POST['itemsJSON']
        amount=request.POST['amount']
        print(itemslist)
        if itemslist == 'null' or itemslist == "{}":
            print('shop first')
        else :
            user=request.user
            order=Orders(name=user.email,address="empty",items=itemslist,oid='random')
            order.save()

            id=order.order_id
            oid=str(id)+'Food.'
            params={   
                'MID':keys.MID,
                'ORDER_ID':oid,
                'TXN_AMOUNT':amount,
                'CUST_ID':user.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'WEBSTAGING',
                "CHANNEL_ID":'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000'
            }
    return  redirect('Home:profile')
    
