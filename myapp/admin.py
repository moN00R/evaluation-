from django.contrib import admin
from myapp.models import User, MyModel

admin.site.register(User)
admin.site.register(MyModel)