from django.contrib import admin
from .models import  *

# Register your models here.

class registerAdmin(admin.ModelAdmin):
    list_display=('email','passwd')

admin.site.register(register,registerAdmin)

class joinsAdmin(admin.ModelAdmin):
    list_display=('Name','Mobile','Email')
admin.site.register(joins,joinsAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display=('Name','Mobile','Email','Message')
admin.site.register(contact,contactAdmin)

class eventAdmin(admin.ModelAdmin):
    list_display = ('id','event_picture','price','dprice','event_date','event_time','event_detail','event_des','event_s','event_e','event_category','event_org','event_mob','event_mail','event_add','event_phn')
admin.site.register(event,eventAdmin)

class booknowAdmin(admin.ModelAdmin):
    list_display=('id','userid','event_name','event_picture','event_date','event_price','booking_date')
admin.site.register(booknow,booknowAdmin)

class videogalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','vlink','vdate','event_des')

admin.site.register(videogallery,videogalleryAdmin)



