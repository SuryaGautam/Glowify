from django.contrib import admin
from contactenquiry.models import ContactEnquiry

class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number','message')
admin.site.register(ContactEnquiry,ContactEnquiryAdmin)
# Register your models here.
