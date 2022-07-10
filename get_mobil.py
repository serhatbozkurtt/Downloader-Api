from pytube import YouTube
import os
from datetime import datetime
from time import gmtime, strftime
import pyrebase


def main(linki):
    print("mobil linki -->> " + linki)
    link = "https://www.youtube.com/watch?v=Y2tw4fNEfbI"
    print("link girildi")

    try:
        yt = YouTube(link)
    except:
        print("Invalid link")
        exit()

    mpt = yt.streams.filter(only_audio=True).first()

    upload(mpt)



def upload(mpt):
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
    # upload
    # storage.child("s.mp3").put("/audio/MySong.mp3")
    # storage.child("gs_up.jpg").put("/static/images/gs.jpg")

    filename1 = 'get_v_flask2'
    filename = datetime.now().strftime('%Y%m%d%H%M%S%f')

    fn = filename + '.mp3'

    output = mpt.download(filename = fn)

    print("storage a geldi")

    storage.child("%s" %fn).put("%s" %fn)

    print("storage bitti")
