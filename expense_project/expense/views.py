from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer
from .forms import ExpenseForm


class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer


class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


def index(request):
    return render(request, 'First_Page.html')


def expense_dashboard(request, pk=None):
    expenses = Expense.objects.all().order_by('-date')
    total_amount = sum(exp.amount for exp in expenses)

    if pk:
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(request.POST or None, instance=expense)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('expense-dashboard')
    else:
        form = ExpenseForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('expense-dashboard')

    context = {
        'expenses': expenses,
        'form': form,
        'edit_id': pk,
        'total_amount': total_amount
    }
    return render(request, 'dashboard.html', context)


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expense-dashboard')
