from django.urls import path
from .views import InvestList, InvestCreate, InvestUpdate, InvestDelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', InvestList.as_view(), name='investments'),
    path('invest-create/', InvestCreate.as_view(), name='invest-create'),
    path('invest-detail/<int:pk>/', DetailView.as_view(), name='invest-detail'),
    path('invest-update/<int:pk>/', InvestUpdate.as_view(), name='invest-update'),
    path('invest-delete/<int:pk>/', InvestDelete.as_view(), name='invest-delete'),
]
