from django.shortcuts import render,redirect
from adminapp.models import Textiles_Db,ProductDb
from webapp.models import ContactDb,RegisterDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index_page(req):
    return render(req,"index.html")
def demo_page(req):
    return render(req,"demo.html")
def save_textiles(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b= req.POST.get('description')
        img=req.FILES['image']
        obj1=Textiles_Db(Category_Name=a,Description=b,Category_Image=img)
        obj1.save()
        messages.success(req,"Category Saved Successfully....!")
        return redirect(demo_page)
def display_textiles(req):
    data = Textiles_Db.objects.all()
    return render(req,"display_textiles.html",{'data':data})
def edit_textiles(req,text_id):
    data=Textiles_Db.objects.get(id=text_id)
    return render(req,"edit_textiles.html",{'data':data})
def update_textiles(req,text_id):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('description')
        try:
          img=req.FILES['image']
          fs=FileSystemStorage()
          file=fs.save(img.name,img)
        except MultiValueDictKeyError:
          file=Textiles_Db.objects.get(id=text_id).Category_Image
        Textiles_Db.objects.filter(id=text_id).update(Category_Name=a,Description=b,Category_Image=file)
        messages.success(req, "Updated Successfully....!")
        return redirect(display_textiles)
def delete_textiles(req,text_id):
    x=Textiles_Db.objects.filter(id=text_id)
    x.delete()
    messages.error(req,'Deleted Successfully....!')
    return redirect(display_textiles)
def Add_product(req):
    category = Textiles_Db.objects.all()
    return render(req,"Add_product.html",{'category':category})
def Display_product(req):
    category = ProductDb.objects.all()
    return render(req,"Display_product.html",{'category':category})
def save_product(req):
    if req.method=="POST":
        a = req.POST.get('cname')
        b= req.POST.get('product_name')
        c = req.POST.get('description')
        d = req.POST.get('price')
        e =req.POST.get('brand_name')
        img1=req.FILES['img1']
        img2=req.FILES['img2']
        img3=req.FILES['img3']
        obj2=ProductDb(CategoryName=a,Product_Name=b,Description=c,Price=d,Brand_Name=e,CategoryImage1=img1,CategoryImage2=img2,CategoryImage3=img3)
        obj2.save()
        messages.success(req, "Product Saved Successfully....!")
        return redirect(Add_product)
def Edit_product(req,pro_id):
    category =Textiles_Db.objects.all()
    products=ProductDb.objects.get(id=pro_id)
    return render(req,"Edit_product.html",{'category':category,'products':products})
def delete_product(req,pro_id):
    x = ProductDb.objects.filter(id=pro_id)
    x.delete()
    messages.error(req, "Deleted Successfully....!")
    return redirect(Display_product)
def update_product(req,pro_id):
    if req.method == "POST":
        a = req.POST.get('cname')
        b = req.POST.get('product_name')
        c = req.POST.get('description')
        d = req.POST.get('price')
        e = req.POST.get('brand_name')
        try:
            img = req.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=pro_id).CategoryImage1
        try:
            img = req.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=pro_id).CategoryImage2
        try:
            img = req.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file3 = ProductDb.objects.get(id=pro_id).CategoryImage3
        ProductDb.objects.filter(id=pro_id).update(CategoryName=a, Product_Name=b,Description=c,Price=d,Brand_Name=e,CategoryImage1=file1,CategoryImage2=file2,CategoryImage3=file3)
        messages.success(req, "Updated Saved Successfully....!")
        return redirect(Display_product)
def admin_page(req):
    return render(req,"admin_page.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome...!")
                return redirect(index_page)
            else:
                messages.warning(request,"Invalid username or password")
                return redirect(admin_page)
        else:
            messages.warning(request, "User not found....!")
            return redirect(admin_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request, "Logout successfully....!")
    return redirect(admin_page)
def contact_details(req):
    data = ContactDb.objects.all()
    return render(req,"contact_details.html",{'data':data})
def delete_contact(req,cn_id):
    x=ContactDb.objects.filter(id=cn_id)
    x.delete()
    messages.error(req, "Contact Removed")
    return redirect(contact_details)
def Register_Details(req):
    data = RegisterDb.objects.all()
    return render(req,"Register_Details.html",{'data':data})

def delete_register(req,cc_id):
    x=RegisterDb.objects.filter(id=cc_id)
    x.delete()
    messages.info(req, "Removed User...!")
    return redirect(Register_Details)
