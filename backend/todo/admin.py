from django.contrib import admin
from .models import Todo
from .models import Person
from .models import PayCheck

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName') 

class PayCheckAdmin(admin.ModelAdmin):
    list_display = ('name', 'hourly', 'totalHours') 

# Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(PayCheck, PayCheckAdmin)
