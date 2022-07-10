import pyrebase

def main():
    config = {
        "apiKey": "AIzaSyBkALe1CYOOfQyLNa7Q2odd0P6LZ91jxrA",
        "authDomain": "ytmp3-f6bcc.firebaseapp.com",
        "projectId": "ytmp3-f6bcc",
        "storageBucket": "ytmp3-f6bcc.appspot.com",
        "messagingSenderId": "5264877193",
        "appId": "1:5264877193:web:a59238198e3e2498e94858",
        "measurementId": "G-ZBX5927KVR",
        "serviceAccount": "serviceAccount.json",
        "databaseURL": "https://ytmp3-f6bcc-default-rtdb.firebaseio.com/"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    #upload
    #storage.child("s.mp3").put("/audio/MySong.mp3")
    #storage.child("gs_up.jpg").put("/static/images/gs.jpg")
    storage.child("1007gsf.jpg").put("gsf.jpg")

    #download
    #storage.download("s.mp3", "down.mp3")