from flask import Flask, jsonify, request
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

@app.route("/down", methods=['GET', 'POST'])
def down():
    if request.method == 'POST':
        req_data = request.get_json()
        print(req_data)
        res = get_mobil.link_js(req_data)
        return jsonify({'video_name':res})
    return jsonify({'todos':'TODOS'})


if __name__ == "__main__":
    app.run()
