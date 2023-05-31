from django.contrib import admin
from appsite.models import FileProperties
from appsite.all_functions import process_file

class FilePropertiesAdmin(admin.ModelAdmin):
    # define fields to display in admin panel
    list_display = ('filename', 'date_added', 'industry_tag','original_url', 'summary_url')

    def save_model(self, request, obj, form, change):
        # generate summary URL using the original URL and filename
        obj.summary_url = process_file(obj.original_url, obj.filename)

        # save the instance to the database
        obj.save()

admin.site.register(FileProperties, FilePropertiesAdmin)

