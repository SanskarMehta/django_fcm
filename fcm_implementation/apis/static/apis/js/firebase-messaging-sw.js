// Give the service worker access to Firebase Messaging.
importScripts('https://www.gstatic.com/firebasejs/8.2.6/firebase-app.js')
importScripts('https://www.gstatic.com/firebasejs/8.2.6/firebase-messaging.js')

var firebaseConfig = {
                  apiKey: "AIzaSyDRxXgvFhVOuzKPRev4VpXu5WAl_0IVNJA",
                  authDomain: "practicefcm-4d02d.firebaseapp.com",
                  databaseURL: "https://practicefcm-4d02d-default-rtdb.firebaseio.com",
                  projectId: "practicefcm-4d02d",
                  storageBucket: "practicefcm-4d02d.appspot.com",
                  messagingSenderId: "441252722793",
                  appId: "1:441252722793:web:2856950bac8fa8dde3caf8",
                  measurementId: "G-JRHJS3GFDE"
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