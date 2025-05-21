from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['tittle', 'amount', 'category', 'date']
        widgets = {
            'date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
