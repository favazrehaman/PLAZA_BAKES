from django.urls import path
from .views import *



urlpatterns=[
    path('ind/', ind),
    path('shopregister/', shopreg),
    path('shoplogin/', shoplog),
    path('userregister/', userreg),
    path('verify/<auth_token>', verify),
    path('userlogin/', userlog),
    path('profile/', profpage),
    path('productupload/', productupload),
    path('productdisplay/', productdisplay),
    path('delete/<int:id>', productdelete),
    path('edit/<int:id>', productedit),
    path('userproddisp/', userproduct),
    path('userprof/', userprof),
    path('addcart/<int:id>', addcart),
    path('wishlistuser/<int:id>', wishlistuser),
    path('wishlistdisplay/', wishlistdisplay),
    path('cartdisplay/', cartdisplay),
    path('removecart/<int:id>', removecart),
    path('wishlistremove/<int:id>', wishlistremove),
    path('cartbuy/<int:id>', cartbuy),
    path('order/<int:id>', order),
    path('customerdetails/', details),
    path('summary/', summary),
    path('shop_notification/',shop_notification),
    path('user_notification/',user_notification)

]