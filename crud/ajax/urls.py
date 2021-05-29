from django.urls import path
from .views import home,detail,add,update,delete

urlpatterns = [
    path('',home,name='home'),
    path('create/',add,name='add'),
    path('delete/<id>/',delete,name='delete'),
    path('update/<id>/',update,name='update'),
    path('<id>/',detail,name='detail'),
]