cart=JSON.parse(localStorage.getItem('cart'))
console.log(cart)

var sum=0;
cartlist="<ul>"
for(var item in cart)
{
    sum+= (cart[item][0]*cart[item][2]);
    cartlist += "<li>item : " + cart[item][1]+  "          quantity : " +cart[item][0] + "        Price : " +cart[item][2]+ " </li>"
}



cartlist += "<li><h2>Total sum : " +sum+"</h2></li>";
cartlist += "</ul>"
cartlist += "</ul>"

msg ="<h1>Empty cart please shop First !</h1>"

if(sum==0){
    document.getElementById('cartlist').innerHTML=msg
}
else{
    document.getElementById('cartlist').innerHTML=cartlist
}

document.getElementById('itemsJSON').setAttribute('value',JSON.stringify(cart));
document.getElementById('amount').setAttribute('value',sum);
document.getElementById('placeorder').addEventListener('click',function(){
localStorage.clear()
})

P_orders=document.getElementsByClassName('prev_order_item');
console.log(P_orders[0].value)

for(itm in P_orders){
    console.log(itm)
}

