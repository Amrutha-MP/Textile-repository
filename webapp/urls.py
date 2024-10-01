from django.urls import path
from webapp import views



urlpatterns=[
    path('Home/',views.Home_page,name="Home"),
    path('AboutUs/',views.Aboutpage,name="AboutUs"),
    path('Contact/',views.Contactpage,name="Contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('All_products/',views.All_products,name="All_products"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
    path('Register/',views.Register_page,name="Register"),
    path('',views.Login_page,name="Login_page"),
    path('save_register/',views.save_register,name="save_register"),
    path('User_Login/',views.User_Login,name="User_Login"),
    path('User_logout/',views.User_logout,name="User_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart/',views.cart_page,name="cart"),
    path('delete_cart/<int:cart_id>/',views.delete_cart,name="delete_cart"),
    path('checkout/',views.checkout_page,name="checkout"),
    path('Payment/',views.Payment_page,name="Payment"),
    path('save_checkout/',views.save_checkout,name="save_checkout")

]