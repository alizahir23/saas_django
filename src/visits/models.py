from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db table name
    #  id primary key
    # 'blank=True' allows this field to be empty in forms/validation (i.e., Django admin, ModelForms)
    # 'null=True' allows this field to store NULL in the database
    path = models.TextField(blank=True, null=True)
    # The 'auto_now_add=True' parameter automatically sets the field to the current timestamp when a new record is created.
    timestamp = models.DateTimeField(auto_now_add=True)
