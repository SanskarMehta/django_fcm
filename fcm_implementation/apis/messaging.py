from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from .models import NotificationMessages


def send_notification(title, message):
    try:
        device = FCMDevice.objects.all()
        notification = FCMDevice.objects.send_message(Message(notification=Notification(title=title, body=message)))
        NotificationMessages.create_notification(title=title, message=message, devices=device)
        return notification
    except Exception as e:
        print(e)
        return None
