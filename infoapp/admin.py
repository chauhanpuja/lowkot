from django.contrib import admin
from .models import Post,StudentUser,Contact,Service,Purchase
# Register your models here.

admin.site.register(Post)
admin.site.register(StudentUser)
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Purchase)

