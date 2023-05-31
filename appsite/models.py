from django.db import models
from all_functions import process_file
from datetime import date
class FileProperties(models.Model):
    industry_choices = [
    ('it', 'IT'),
    ('food', 'Food'),
    ('medicine', 'Medicine'),
    ('general','General'),
    ]
    filename = models.CharField(max_length=255)
    date_added = models.DateField(default=date.today)
    industry_tag = models.CharField(max_length=255, choices=industry_choices, default='general')
    original_url = models.CharField(max_length=255)
    summary_url = models.CharField(max_length=255, blank=True)
    

    def save(self, *args, **kwargs):
        # Call the process_file function to download the file and update summary_url
        self.summary_url = process_file(self.original_url, self.filename)
        super().save(*args, **kwargs)
        
