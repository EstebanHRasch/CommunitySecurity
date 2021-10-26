from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'console'
urlpatterns = [
    path('CameraList', views.CameraView.as_view()),
    path('FootageList/camera/<int:camera_id>/date/<slug:footage_date>', views.FootageView.as_view()),
    path('AccessList/camera/<int:camera_id>', views.access_instanceView.as_view())
    #path('<str:camera_id>/', views.ArchivesPage.as_view(), name='select_camera'),#name = 'function being called in views.py'
    #path('<str:camera_id>/<int:date>/', views.ArchivesPage.as_view(), name='select_date'),  #The arguments in path are the arguments in views.py
    #path('<str:camera_id>/<int:date>/<int:time>/', views.ArchivesPage.as_view(), name='select_time'),
    #path('signup', views.signup, name='signup'),
    #path('login', views.userLogin, name='login'),
    #path('logout', views.logout_request, name='logout'),
    #path('createFootage', csrf_exempt(views.createFootage), name='createFootage'),
]
