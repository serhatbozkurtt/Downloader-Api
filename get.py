from pytube import YouTube
import os
import pyrebase


def main():
    #link = input("Link: ")
    #directory = input("Directory: ")
    link = "https://www.youtube.com/watch?v=Ab5g3Ug7ysM"
    print("link girildi")

    try:
        yt = YouTube(link)
        print("try catch")
    except:
        print("Invalid link")
        exit()

    mpt = yt.streams.filter(only_audio=True).first()

    print("convert")
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
    print("configi geçti")
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # upload
    # storage.child("s.mp3").put("/audio/MySong.mp3")
    # storage.child("gs_up.jpg").put("/static/images/gs.jpg")

    output = mpt.download(filename='get_v_flask2.mp3')

    print("stroage a geldi")

    storage.child("mpt.mp3").put("get_v_flask2.mp3")

    print("stroage bitti")





    ''' print("Downloading...")

    output = mp3.download(output_path='C:/Users/Serhat/Programming/PycharmProjects/mp3_db/venv/Include/audio', filename='MySong')

    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output, to_mp3)

    print("Download complete")'''


def conv(link):
    print("link--->> " + link)
    print("Downloading... converter")
    return "return"
