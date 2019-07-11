from django.contrib import admin
from user.models import User, Role, Jurisdiction, Section
# Register your models here.


admin.site.register(User)
admin.site.register(Role)
admin.site.register(Jurisdiction)
admin.site.register(Section)

