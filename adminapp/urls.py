from django.urls import path
from adminapp import views


urlpatterns =[
    path('index_page/',views.index_page,name="index_page"),
    path('demo_page/',views.demo_page,name="demo_page"),
    path('save_textiles/',views.save_textiles,name="save_textiles"),
    path('display_textiles/',views.display_textiles,name="display_textiles"),
    path('edit_textiles/<int:text_id>/',views.edit_textiles,name="edit_textiles"),
    path('update_textiles/<int:text_id>/',views.update_textiles,name="update_textiles"),
    path('delete_textiles/<int:text_id>/',views.delete_textiles,name="delete_textiles"),
    path('Add_product/',views.Add_product,name="Add_product"),
    path('Display_product/',views.Display_product,name="Display_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('Edit_product/<int:pro_id>/',views.Edit_product,name="Edit_product"),
    path('delete_product/<int:pro_id>/',views.delete_product,name="delete_product"),
    path('update_product/<int:pro_id>/',views.update_product,name="update_product"),
    path('admin_page/',views.admin_page,name="admin_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:cn_id>/',views.delete_contact,name="delete_contact"),
    path('Register_Details/',views.Register_Details,name="Register_Details"),
    path('delete_register/<int:cc_id>/',views.delete_register,name="delete_register")
]