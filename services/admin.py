from django.contrib import admin

# Register your models here.
from .models import Person, Meetingtime, Service, Question

admin.site.register(Person)
admin.site.register(Meetingtime)
admin.site.register(Service)
admin.site.register(Question)