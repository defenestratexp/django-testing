import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# class of available operating system versions
class OperatingSystemVersion(models.Model):
    os_version = models.CharField(max_length=5)

    def __str__(self):
        return self.os_version

# Class containing list of operating systems
class OperatingSystem(models.Model):
    os_name = models.CharField(max_length=50)
    os_sys_version = models.ForeignKey(OperatingSystemVersion)

    # Add a __str__ method
    def __str__(self):
        return self.os_name

# Class of Purpose listings for an AMI
class OpSysPurpose(models.Model):
    os_purpose_name = models.CharField(max_length=50)

    def __str__(self):
        return self.os_purpose_name

# class of AMI data
class Ami(models.Model):
    ami_name = models.CharField(max_length=25, default="Empty")
    ami_id = models.CharField(max_length=12)
    ami_creation_date = models.DateTimeField('date created')
    ami_os_system = models.ForeignKey(OperatingSystem)
    ami_os_version = models.ForeignKey(OperatingSystemVersion)
    ami_purpose = models.ForeignKey(OpSysPurpose)

    def __str__(self):
        return self.ami_id

    def was_created_recently(self):
        return self.ami_creation_date >= timezone.now() - datetime.timedelta(days=1)
        # These attributes allow more functionality in the admin view
        was_created_recently.admin_order_field = 'ami_creation_date'
        was_created_recently.boolean = True
        was_created_recently.short_description = 'Created Recently?'
