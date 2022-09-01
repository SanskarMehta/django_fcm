// Give the service worker access to Firebase Messaging.
importScripts('https://www.gstatic.com/firebasejs/8.2.6/firebase-app.js')
importScripts('https://www.gstatic.com/firebasejs/8.2.6/firebase-messaging.js')

var firebaseConfig = {
                  apiKey: "<YOUR_API_KEY>",
                  authDomain: "<YOUR_AUTH_DOMAIN>",
                  databaseURL: "<YOUR_DATABASE_URL>",
                  projectId: "<YOUR_PROJECT_ID>",
                  storageBucket: "<YOUR_STORAGE_BUCKET>",
                  messagingSenderId: "<YOUR_MESSAGING_SENDER_ID>",
                  appId: "<YOUR_APP_ID>",
                  measurementId: "<YOUR_MEASUREMENT_ID>"
        };


firebase.initializeApp(firebaseConfig);
// Retrieve an instance of Firebase Data Messaging so that it can handle background messages.
const messaging = firebase.messaging()
messaging.setBackgroundMessageHandler(function (payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    const notificationTitle = 'Data Message Title';
    const notificationOptions = {
        body: 'Data Message body',
        icon: 'alarm.png'
    };

    // console.log(notificationTitle);
    return self.registration.showNotification(notificationTitle,
        notificationOptions);
});
if (firebase.messaging.isSupported()) {
  firebase.messaging();
}