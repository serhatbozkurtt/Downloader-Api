from flask import Flask, jsonify, request, render_template
import get
import get_mobil
import get_web
from flask import send_file

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

@app.route("/web", methods=['GET', 'POST'])
def web():
    if request.method == 'POST':
        link = request.form.get("link")
        print("link " + link)
        response = get_web.main(link)
        #response = "20220710134318014559.mp3"
        filename = response
        #with open('/tmp/output.mp3', 'wb') as out:
        #    out.write(response.audio_content)

        return send_file("%s" %filename, as_attachment=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
