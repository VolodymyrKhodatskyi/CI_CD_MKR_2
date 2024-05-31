from django.urls import path

from recipe import views

app_name = "recipe"

urlpatterns = [
	path('', views.main, name='main'),
    path('category_list/', views.category_list, name='category_list'),
]