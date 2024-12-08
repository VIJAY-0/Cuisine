from django.shortcuts import render,redirect
from home.models import *
from home import  keys
import json


# Create your views here.home

def home(request):
    # return HttpResponse('Hello')
    items=Items.objects.all()
    category=Category.objects.all()
    context={'items':items,
             'category':category}
    return render(request,'index.html',context)

def place_order_page(request):
    print("cart checkout ckicked")
    items=Items.objects.all()
    category=Category.objects.all()
    context={'items':items,
             'category':category}
    return render(request,'place_order.html',context)

def profile(request):
    print("Profile page loadec")
    user=request.user
    placed_orders=Orders.objects.filter(name=user.email)
    ORDERS=[]
    for order in placed_orders:
        itemJSON=json.loads(order.items)
        order=[]
        order_total =0
        for key, value in itemJSON.items():
            tot_amnt_per_item=0
            tot_amnt_per_item=float(value[0])*float(value[2])
            order_total+=tot_amnt_per_item
            order.append([value[0],value[1] ,tot_amnt_per_item])
            order_total+=tot_amnt_per_item
        ORDERS.append([order,order_total])
    context={'prev_orders':ORDERS}
    return render(request,'profile.html',context)

def reciveOrder(request):
    print("place order clicked")
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
            print(oid)
    return  redirect('Home:profile')
    
