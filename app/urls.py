from django.urls import path
from app import views
from app.views import *



urlpatterns = [
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('', views.login, name='login'),
    # path('upload', views.upload, name='upload'),
    path('documents', views.document_list, name='documents'),
    path('thankyou', views.thank_you, name= 'thankyou'),
]