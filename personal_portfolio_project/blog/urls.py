from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:post_id>/', views.detail, name='detail'),
]
