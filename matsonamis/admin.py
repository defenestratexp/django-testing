from django.contrib import admin

from .models import *
# Register your models here.
# admin.site.register(modelname, modelnameview)
# if more than one model is required you need an admin.site.register
# for each one

# Add admin classes here
class OperatingSystemAdmin(admin.ModelAdmin):
    # This is the default method of including fields
    #fields= ['os_name', 'os_sys_version']

    #This one labels them
    fieldsets = [
            ('OS Name', {'fields': ['os_name']}),
            ('OS Version', {'fields': ['os_sys_version']}),
            ]

    list_display = ('os_name', 'os_sys_version')
    list_filter = ['os_name']
    search_fields = ['os_name']

class AmiAdmin(admin.ModelAdmin):
    fieldsets =[
            ('Name', {'fields': ['ami_name']}),
            ('ID', {'fields': ['ami_id']}),
            ('OS', {'fields': ['ami_os_system', 'ami_os_version']}),
            ('Purpose', {'fields': ['ami_purpose']}),
            ('Created On', {'fields': ['ami_creation_date'], 'classes': ['collapse']}),
            ]

    list_display = ('ami_name', 'ami_id', 'ami_os_system', 'ami_os_version', 'ami_purpose', 'was_created_recently')

    list_filter = ['ami_creation_date']
    search_fields = ['ami_id']

# Changes to admin.py are not reflected until the server is restarted.
admin.site.register(OperatingSystemVersion)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(OpSysPurpose)
admin.site.register(Ami, AmiAdmin)
