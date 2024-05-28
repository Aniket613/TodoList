from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home-page'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('Delete-task/<str:name>',views.DeleteTask,name='delete'),
    path('Update/<str:name>',views.Update,name='update'),

]