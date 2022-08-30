from django.db import models
from fcm_django.models import FCMDevice


class NotificationMessages(models.Model):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    device = models.ForeignKey(FCMDevice, on_delete=models.CASCADE)


    def get_device_object(self, registration_id):
        return FCMDevice.objects.filter(registration_id=registration_id).first()

    @classmethod
    def create_notification(cls, title, message, devices):
        for i in devices:
            notify = cls.objects.create(title=title, message=message, device=i)
            notify.save()
        return "Created Successfully"
