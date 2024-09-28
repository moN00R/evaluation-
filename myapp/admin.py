from django.contrib import admin
from myapp.models import User, MyModel, ConfigurationModel

admin.site.register(User)
admin.site.register(MyModel)
admin.site.register(ConfigurationModel)