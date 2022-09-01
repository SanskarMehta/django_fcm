from django.db import models
from fcm_django.models import FCMDevice


class NotificationMessages(models.Model):
    """
    This class is a model of Notifications.
    title -> Charfield : Consist the title of messages
    message -> Charfield : Consist the body of messages
    device -> foreignkey : It holds the object of FCMDevice model where different devices are registered.
    """
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    device = models.ForeignKey(FCMDevice, on_delete=models.CASCADE)


    def get_device_object(self, registration_id):
        """
        It is a method which executes the query and return the specific object of FCMDevice tabel.
        :param registration_id: It is a registration token of device which are registered in table.
        :return: Object of FCMDevice model.
        """
        return FCMDevice.objects.filter(registration_id=registration_id).first()

    @classmethod
    def create_notification(cls, title, message, devices):
        """
        It saves the data in model.
        :param title: Consist the title of messages
        :param message: Consist the body of messages
        :param devices: It holds the object of FCMDevice model where different devices are registered.
        :return: Returns the created succefully message
        """
        for i in devices:
            notify = cls.objects.create(title=title, message=message, device=i)
        return "Created Successfully"
