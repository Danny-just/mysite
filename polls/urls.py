from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'hello/', views.hello, name='hello'),
    url(r'getStudent/',views.getStudent, name='getStudent'),

]