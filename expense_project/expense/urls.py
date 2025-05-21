from django import views
from django.urls import path
from . import views
# from .views import (
#     ExpenseListCreateAPIView,
#     ExpenseRetrieveUpdateDestroyAPIView,
#     index
# )
urlpatterns = [
    # path('', index, name='index'),  # Home page showing template
    # path('expense/', ExpenseListCreateAPIView.as_view(),
    #      name='expense-list-create'),  # plural 'expenses' is common convention
    # path('expense/<int:pk>/',
    #      ExpenseRetrieveUpdateDestroyAPIView.as_view(), name='expense-detail'),

    path('', views.expense_dashboard, name='expense-dashboard'),
    path('<int:pk>/', views.expense_dashboard, name='expense-dashboard-edit'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),]
