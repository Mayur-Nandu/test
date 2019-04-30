import pyrebase
config = {
    "apiKey": "AIzaSyD3AKt54QUkjbd9B8CaZ8ksg5y7fRzZV1s",
    "authDomain": "connect-to-gcp-new.firebaseapp.com",
    "databaseURL": "https://connect-to-gcp-new.firebaseio.com",
    "projectId": "connect-to-gcp-new",
    "storageBucket": "connect-to-gcp-new.appspot.com",
    "messagingSenderId": "779277451716"
  };
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
#storage.child("obj/obj.ply").put("2.ply")
storage.child("obj/obj.ply").download('object.ply')
