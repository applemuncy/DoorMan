from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    # Other fields here
    rfid_access = models.BooleanField(default=False)
    rfid_tag = models.CharField(max_length=20,blank=True,null=True,unique=True)
    #rfid_in_eeprom = models.BooleanField(default=False) # changed from slot, which was unwieldy to manage.

    rfid_label = models.CharField(max_length = 50) # little label on the tag
    update_date = models.DateTimeField(null=True, blank = False, auto_now = True) # taking matters into my own hands...
    sync_date = models.DateTimeField(null=True, blank=True, auto_now = True, )
    #syncing = models.IntegerField(default = 0)

    def save(self, *args, **kwargs):
        print ("in da save, son")
        try:
            mask = 255 # actually this is the 'locked out' - 0 is the 'just log it'
            existing = UserProfile.objects.all().get(user=self.user)

            self.id = existing.id #force update instead of insert
            if (self.rfid_access):
                mask = 1
            print ("going for the EEPROM mod")
            if rfid_sock.modify_user(local_settings.RFID_HOST, local_settings.RFID_PORT, self.rfid_tag, mask, local_settings.RFID_PASSWORD):
                self.sync_date = datetime.now()
            # also set synch date, synching

        except UserProfile.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

    def __str__(self):
        return self.user.username

"""

for storing when we let ppl in

"""

class AccessEvent(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,)
    event_date = models.DateTimeField(auto_now = True)
    def __str__(self):
        u=self.user
        ud = self.event_date
        n=u.__str__()
        d= ud.__str__()
        return "    ".join([ n, d])


