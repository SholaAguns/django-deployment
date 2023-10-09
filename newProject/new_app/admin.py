from django.contrib import admin

from new_app.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)


