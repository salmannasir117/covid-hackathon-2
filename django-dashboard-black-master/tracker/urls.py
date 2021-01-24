from django.urls import path

from . import views

app_name = 'tracker' #adds a namespace

urlpatterns = [
    #path('', views.test_static, name="static-test"),
    path('list_tests/', views.list_tests, name="list_tests"),
    path('list-tests/', views.list_tests2, name="list-tests"),
    path('download_template/', views.download_template, name='download_template'),
    path('upload/', views.upload_file, name='upload_file'),
]