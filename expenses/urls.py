from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='list'),
    path('add/', views.ExpenseCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', views.ExpenseUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='delete'),
]
