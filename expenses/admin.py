
from django.contrib import admin
from expenses.models import *

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('catergory', 'amount', 'date' )





admin.site.register(Expense)