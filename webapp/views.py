from django.shortcuts import render,redirect
from webapp.models import ContactDb,RegisterDb,CartDb,Checkout_DB
from adminapp.models import Textiles_Db,ProductDb
from django.contrib import messages
import razorpay

# Create your views here.
def Home_page(req):
    cat = Textiles_Db.objects.all()
    products = ProductDb.objects.all()
    return render(req,"Home.html",{'cat':cat,'products':products})
def Aboutpage(req):
    cat = Textiles_Db.objects.all()
    return render(req,"About_Us.html",{'cat':cat})
def Contactpage(req):
    cat = Textiles_Db.objects.all()
    return render(req,"Contact.html",{'cat':cat})

def save_contact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        ms=req.POST.get('message')
        obj = ContactDb(Name=na,Email_Id=em,Message=ms)
        obj.save()
        messages.success(req,"Message sent successfully...!")
        return redirect(Contactpage)
def All_products(req):
    cat = Textiles_Db.objects.all()
    products=ProductDb.objects.all()
    return render(req,"All_products.html",{'products':products,'cat':cat})
def single_product(req,pro_id):
    cat = Textiles_Db.objects.all()
    product=ProductDb.objects.get(id=pro_id)
    return render(req,"single_product.html",{'product':product,'cat':cat})
def filtered_product(req,cat_name):
    cat = Textiles_Db.objects.all()
    data=ProductDb.objects.filter(CategoryName=cat_name)
    return render(req,"filtered_product.html",{'data': data,'cat':cat})
def Register_page(req):
    return render(req,"Registration.html")
def Login_page(req):
    return render(req,"Login.html")
def save_register(req):
    if req.method == "POST":
        un=req.POST.get('name')
        em=req.POST.get('email')
        ps=req.POST.get('password')
        cp=req.POST.get('cpassword')
        obj1 = RegisterDb(User_Name=un, Email=em, Password=ps,CPassword=cp)
        obj1.save()
        messages.success(req,"Registered Successfully..")
        return redirect(Register_page)
def User_Login(request):
    if request.method=="POST":
        un = request.POST.get('name')
        ps = request.POST.get('password')
        if RegisterDb.objects.filter(User_Name=un,Password=ps).exists():
            request.session['User_Name']=un
            request.session['Password']=ps
            messages.success(request,"Welcome..")
            return redirect(Home_page)
        else:
            messages.warning(request,"Invalid user or password")
            return redirect(Login_page)
    else:
        # messages.warning(request, "Invalid user")
        return redirect(Login_page)
def User_logout(request):
    del request.session['User_Name']
    del request.session['Password']
    messages.error(request, "Logout successfully")
    return redirect(Home_page)
def save_cart(request):
    if request.method == "POST":
        un=request.POST.get('name')
        pn=request.POST.get('productname')
        qn=request.POST.get('quantity')
        pc=request.POST.get('price')
        tp=request.POST.get('totalprice')
        obj1 = CartDb(User_Name=un,Product_Name=pn,Quantity=qn, Price=pc, Total_price=tp)
        obj1.save()
        messages.success(request,"Added to Cart..")
        return redirect(Home_page)
def cart_page(request):
    cat = Textiles_Db.objects.all()
    data=CartDb.objects.filter(User_Name=request.session['User_Name'])
    sub_total=0
    shipping=0
    total=0
    for i in data:
        sub_total += i.Total_price
    if sub_total>500:
        shipping=150
    else:
        shipping=250
    total = sub_total+shipping
    return render(request,"cart.html",{'data':data,'cat':cat,'sub_total':sub_total,'shipping':shipping,'total':total})
def delete_cart(req,cart_id):
    x = CartDb.objects.filter(id=cart_id)
    x.delete()
    messages.info(req, "Item removed from cart..!")
    return redirect(cart_page)
def checkout_page(request):
    cat = Textiles_Db.objects.all()
    data=CartDb.objects.filter(User_Name=request.session['User_Name'])
    sub_total = 0
    shipping = 0
    total = 0
    for i in data:
        sub_total += i.Total_price
    if sub_total > 500:
        shipping = 150
    else:
        shipping = 250
    total = sub_total + shipping
    return render(request,"checkout.html",{'data':data,'sub_total':sub_total,'shipping':shipping,'total':total,'cat':cat})
def Payment_page(request):
    customer=Checkout_DB.objects.order_by('-id').first()
    payy=customer.Total_price
    amount=int(payy*100)
    payy_str=str(amount)

    for i in payy_str:
        print(i)

    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_oVF8wJ5V3HMhtw','dJzANZczPrdD0sYFoztgOpS8'))
        payment=client.order.create({'amount':amount,'currency':order_currency})

    return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})
def save_checkout(request):
    if request.method == "POST":
        un = request.POST.get('name')
        em=request.POST.get('email')
        pl=request.POST.get('place')
        ad=request.POST.get('address')
        mb=request.POST.get('mobile')
        ms=request.POST.get('message')
        tp=request.POST.get('price')
        obj7 =Checkout_DB(User_Name=un,Email=em,Place=pl,Address=ad,Mobile=mb,Message=ms , Total_price=tp)
        obj7.save()
        return redirect(Payment_page)
