from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('BILLS', 'Bills'),
        ('TRAVEL', 'Travel'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('OTHER', 'Other'),
    ]
    tittle = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'expense_expense'
