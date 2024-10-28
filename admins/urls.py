from django.urls import path
from .views import AdminUser, ProductredView
urlpatterns =[
    path('', AdminUser.as_view()),
    path('redirect/', ProductredView.as_view()),
]