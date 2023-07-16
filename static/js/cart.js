
if (localStorage.getItem('cart')==null)
{
    var cart={}
    console.log("new cart object created\n")
    localStorage.setItem('cart',JSON.stringify(cart))
}

else{
    cart = JSON.parse(localStorage.getItem('cart'))
    updateCart(cart);
}


$('#checkout').on('click',function(){
    console.log(this)
    var url =this.getAttribute("cstmlink");
    console.log(url)
    window.location.href = url;

})


$('.addtocart').on('click',addtocart)
$('#clearcart').on('click',clearCart)

function addtocart()
{
    var idstr = this.id.toString();
    
    if( cart[idstr]!=undefined){
        qty = cart[idstr][0]+1;
    }
    else{
        qty=1;
        nam=document.getElementById('name'+idstr).innerHTML;
        price=document.getElementById('price'+idstr).innerHTML;;
        cart[idstr]=[qty,nam,price];
    }
    localStorage.setItem('cart',JSON.stringify(cart)) ;
    updateCart(cart);
}

function clearCart(){
    console.log("####    CLEAR CART    ######")
    cart=JSON.parse(localStorage.getItem('cart'))
    for(var item in cart){
        document.getElementById('addtocartP'+item.toString()).innerHTML = "<div class='addtocart' id='"+item+"'>Add to cart</div>"
        $("#"+item).on('click',addtocart)
    }
    cart={}
    localStorage.clear();
    updatePopover(cart);
}

function updatePopover(cart){
    var popstr=""
    popstr+= " <h2>My cart</h2> <br>"
    for(var item in cart){
        popstr+= "<li>";
        popstr+= "<b>" + document.getElementById('name'+item).innerHTML.slice(0,19)+" </b>";
        popstr+= "..." + cart[item][0] +" Qty";
        popstr+= "</li>";
    }
    document.getElementById('itemslist').innerHTML=popstr;
    document.getElementById('cartbtn').click();
}

function plus()
{
    id=this.id.toString().slice(4)
    cart[id][0]+=1;
    document.getElementById('val'+id).innerHTML=cart[id][0];
    localStorage.setItem('cart',JSON.stringify(cart));
    updatePopover(cart);
}
function minus()
{
    id=this.id.toString().slice(5)
    if(cart[id][0]==1){
        document.getElementById('addtocartP'+id).innerHTML = "<div class='addtocart' id='"+id+"'>Add to cart</div>"
        $("#"+id).on('click',addtocart)
        delete cart[id];
        
    }
    else{
        cart[id][0]-=1;
        document.getElementById('val'+id).innerHTML=cart[id][0];
    }
    localStorage.setItem('cart',JSON.stringify(cart));
    updatePopover(cart);

}
  


function updateCart(cart)
{
    for (var item in cart){
        document.getElementById('addtocartP'+item.toString()).innerHTML = " <button id= 'minus" +item+ "'  class='btn_incedecre' > - </button>  <span id ='val"+item+"'>"+cart[item][0]+  " </span> <button id= 'plus"+item+"'  class='btn_incedecre' > + </button>" ;
        $("#minus"+item).on('click',minus)
        $("#plus"+item).on('click',plus)
    }
    localStorage.setItem('cart',JSON.stringify(cart));
    updatePopover(cart);
}




  
    