from flask import Flask
import get
import get_mobil

app = Flask(__name__)

@app.route("/")
def baslangic_ap():
    return "Flask Api 3 Denemesi"


@app.route("/mobil/<string:link>")
def begin_mobil(link):
    get_mobil.main(link)
    return "mobil link: " + link


if __name__ == "__main__":
    app.run()
