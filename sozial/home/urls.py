from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profilepage/<pk>', views.profilepage, name='profilepage'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('posting', views.posting, name='posting'),
    path('comment/<pk>', views.comment, name='comment'),
    path('like_post', views.like_post, name='like_post'),
    path('reply_comment/<pk>', views.reply_comment, name='reply_comment'),
    path('following', views.following, name='following'),
   
]
