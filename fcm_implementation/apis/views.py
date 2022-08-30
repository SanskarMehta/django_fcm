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
    def get(self, request, *args, **kwargs):
        return render(request, 'api/index.html')

    def post(self, request, *args, **kwargs):
        request_data = request.read()
        form_data = json.loads(request_data.decode('utf-8'))
        registration_id = form_data.get("registration_id")
        try:
            if not FCMDevice.objects.filter(registration_id=registration_id).exists():
                a = FCMDevice.objects.create(registration_id=registration_id)
                a.save()
                print('Id is registered')
            else:
                print('Id is already there.')
        except Exception as e:
            print(e)
        return JsonResponse({'Success':'Response is shared'})


class Index1(View):
    def get(self, request, *args, **kwargs):
        send_notification(title='Helloo', message="I am doing this for testing of FCM Django")
        return HttpResponse('sent successfully.')


class Index2(View):
    def get(self, request, *args, **kwargs):
        send_notification(title='Helloo', message="I am Sanskar Mehta")
        return HttpResponse('sent successfully.')


# class showFirebaseJS(View):
#     def get(self, request, *args, **kwargs):
#         data = 'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
#                'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
#                'var firebaseConfig = {' \
#                '        apiKey: "AIzaSyDRxXgvFhVOuzKPRev4VpXu5WAl_0IVNJA",' \
#                '        authDomain: "practicefcm-4d02d.firebaseapp.com",' \
#                '        databaseURL: "https://practicefcm-4d02d-default-rtdb.firebaseio.com",' \
#                '        projectId: "practicefcm-4d02d",' \
#                '        storageBucket: "practicefcm-4d02d.appspot.com",' \
#                '        messagingSenderId: "441252722793",' \
#                '        appId: "1:441252722793:web:2856950bac8fa8dde3caf8",' \
#                '        measurementId: "G-JRHJS3GFDE"' \
#                ' };' \
#                'firebase.initializeApp(firebaseConfig);' \
#                'const messaging=firebase.messaging();' \
#                'messaging.setBackgroundMessageHandler(function (payload) {' \
#                '    console.log(payload);' \
#                '    const notification=JSON.parse(payload);' \
#                '    const notificationOption={' \
#                '        body:notification.body,' \
#                '        icon:notification.icon' \
#                '    };' \
#                '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
#                '});'
#         return HttpResponse(data, content_type="text/javascript")