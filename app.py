from flask import Flask,render_template,jsonify
import threading
import detect
from database import get_logs

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plate")
def plate():
    return jsonify({
        "plate": detect.latest_plate,
        "status": detect.status
    })

@app.route("/logs")
def logs():
    return jsonify(get_logs())

def run_camera():
    detect.detect_camera()

if __name__=="__main__":
    threading.Thread(target=run_camera).start()
    app.run(debug=True)