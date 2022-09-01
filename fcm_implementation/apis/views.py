import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from fcm_django.models import FCMDevice
from .messaging import send_notification


@method_decorator(csrf_exempt, name='dispatch')
class Home(View):
    """
    This is a view which is used to register the device in FCMDevice table..
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'api/index.html')

    def post(self, request, *args, **kwargs):
        """
        Basically this method is used to store the registration token.
        :param request: Request consist the JSON type data in which registration token is stored.
        :param args:
        :param kwargs:
        :return: It returns JSONResponse for success of AJAX call.
        """
        request_data = request.read()
        form_data = json.loads(request_data.decode('utf-8'))
        registration_id = form_data.get("registration_id")
        try:
            if not FCMDevice.objects.filter(registration_id=registration_id).exists():
                a = FCMDevice.objects.create(registration_id=registration_id)
                print('Id is registered')
            else:
                print('Id is already there.')
        except Exception as e:
            print(e)
        return JsonResponse({'Success':'Response is shared'})


class Index1(View):
    """
    This is a view which is used to send the notification using FCM.
    """
    def get(self, request, *args, **kwargs):
        send_notification(title='Helloo', message="I am doing this for testing of FCM Django")
        return HttpResponse('sent successfully.')


class Index2(View):
    """
    This is a view which is used to send the notification using FCM.
    """
    def get(self, request, *args, **kwargs):
        send_notification(title='Helloo', message="I am Sanskar Mehta")
        return HttpResponse('sent successfully.')
