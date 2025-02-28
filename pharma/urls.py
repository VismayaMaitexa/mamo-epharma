from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="front"),
#login_page_admin
    path('about/',views.abouts,name='about'),
    path('admins/',views.admin,name='admi'),
    path('buy/',views.buy,name='buys'),
    path('userr/',views.user,name='users'),
    path('contact/',views.contact,name='contact'),

    path('adminlo/',views.admin_login,name='login'),
    path('admin-home',views.adminhome_view,name='admin-home'),
#inside_admin_login_page
    path('prod/',views.product,name='products'),
    path('orde/',views.orders,name='orders'),
    path('user/',views.users,name='user'),
    path('feedback admin/',views.feebback,name='feeds'),
    
    path('log',views.log_out,name='logout'),

#register and login of user
    path('reg/',views.register,name='registers'),    
    path('reg/userlogin',views.userlogin_view,name='userlogin'),

#user_dashboard_register
    path('userdash_reg',views.user_dashboard,name='user_dashh'),

#user_dashboard_login_inn
    path('purchase_bar',views.purchase_item,name='purchase'),

    path('order-user',views.order_user,name='user-order'),

#register and login of  online delivery 
    path('buys_register',views.online_register,name='online_registers'),
    path('buys_logins',views.online_login,name='login__online'),

#login_of online delivery boy
    path('dashboard delivery',views.delivery_dash,name='delivery_boy'),

#admin_user_container_box
   path('user_dash_add',views.inuser_add,name='add-inuser'),
   path('user_dash_view',views.user_in_views,name='view_user_in'),

#admin_user_ delete customer
   path('delete-customer/<int:pk>',views.delete_customer_view,name='delete-customer'),
#admin_user_ view customer
   path('view-customer',views.view_customer_view,name='view-customer'),
#admin_user update customer
   path('update-customer/<int:pk>',views.update_customer_view,name='update-customer'),

#admin_product_adding product
   path('add-products',views.product_adding,name='adds-product'),
#admin_product_viewing product
   path('product view',views.product_viewing,name='product-views'),

#admin_product_viewing delete
   path('delete-product/<int:pk>',views.product_delete,name='delete-products'),
#admin_product_viewing update
   path('update-product/<int:pk>',views.product_update,name='update-products'),

#add_to_cart_in user dash
  path('adding to cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
#add_to_cart_view cart
  path('view cart',views.cart_view,name='viewing_cart'),

#proced_to chehckout user button
  path('proceed button',views.proced_user_checkout,name='proceed button'),
#remove from add from cart
  path('delete-item-cart/<int:pk>',views.cart_deletee,name='item-delete'),


#confirm and payments
  path('payment',views.confirm_payment,name='payments'),
#credit card page with card number/cv code
  path('confirm payment',views.credit_payment,name='credits payment done '),
 
#feedback in user side
  path('feedback user',views.user_feedback,name='user-feedback'),
#thank u page after submit in user
  path('submission',views.thanks,name='thank you'),


#online boy at admin side 
path('delivery_views',views.online_boy_admine,name='admin_online'),
path('approve/<int:id>/', views.approve_delivery_boy, name='approve_delivery_boy'),
path('reject/<int:id>/', views.reject_delivery_boy, name='reject_delivery_boy'),

#online dashboard for delivery boys
path('dashboard boy',views.delivery_dashboard,name='delivery boy dashboard'),

#online delivery boy dashboard_update the status 
 path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
 
#prescription adding in the purch item
path('prescription',views.image,name='images'),

#forgot password in user
path('forgot-password/', views.forgot_password, name='forgot_password'),


#chatbhot
path('chat-bhot',views.chatbhot,name='chat'),


#examples
  path('html/',views.htmls),
  path('sam/',views.sample),


]
