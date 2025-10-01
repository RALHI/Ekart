from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
  list_display = ('email','username','first_name','last_name')
  search_fields = ('email','username','first_name','last_name')

admin.site.register(Account, AccountAdmin)
