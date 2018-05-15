from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^generator/', views.generator, name='generator'),
    url('^generated/', views.generated, name='generated')
]
