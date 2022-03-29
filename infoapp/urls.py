from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="index" ),
    path('about',views.about,name="about" ),
    path('service',views.service,name="service" ),
    path('service_details/<str:slug>',views.service_details,name="service_details" ),
    path('team',views.team,name="team" ),
    path('contact',views.contact,name="contact" ),
    path('purchase',views.purchase,name="purchase"),
    path('userlogin',views.userlogin,name="userlogin" ),
    path('userlogout',views.userlogout,name="userlogout" ),
    path('usersignup',views.usersignup,name="usersignup" ),
    path('blog',views.blog,name="blog" ),
    path('add_post',views.add_post,name="add_post" ),
    path('add_post2',views.add_post2,name="add_post2" ),
    path('blog_details/<str:slug>',views.blog_details,name="blog_details" ),
    path('userpost_details/<str:slug>',views.userpost_details,name="userpost_details" ),
    path('post_list',views.post_list,name="post_list" ),
    path('edit_post/<int:id>',views.edit_post,name="edit_post" ),
    path('edit_post2/<int:id>',views.edit_post2,name="edit_post2" ),
    path('changeimage/<int:id>',views.changeimage,name="changeimage"),
    path('delete_post/<int:id>',views.delete_post,name='delete_post')





    

]