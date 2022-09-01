from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from .models import NotificationMessages


def send_notification(title, message):
    """
    This is a generic function which is used to execute the sending notifications using FCM.
    :param title: Basically It is the title of Notification which will be displayed
    :param message: Basically It is the message of Notification which will be displayed
    :return: It returns the notification object.
    """
    try:
        device = FCMDevice.objects.all()
        notification = FCMDevice.objects.send_message(Message(notification=Notification(title=title, body=message)))
        NotificationMessages.create_notification(title=title, message=message, devices=device)
        return notification
    except Exception as e:
        print(e)
        return None
