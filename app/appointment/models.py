from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Appointment(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    office_name=models.CharField(_('office_name'),max_length=255,blank=True,null=True)
    rfid=models.CharField(_('rfid'),max_length=255,blank=True,null=True)
    description=models.CharField(_('description'),max_length=255,blank=True,null=True)
    date_appointment=models.DateTimeField(_('date_appointment'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
