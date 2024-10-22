from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('post/<int:id>', views.detail, name='detail')
]
