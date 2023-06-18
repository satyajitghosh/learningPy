from flask import Flask,jsonify,render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname),str(ip)

@app.route("/")
def hello_world():
    return "<p> Hello World. </p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
        )

@app.route("/details")
def details():
    # Automatically detects the index.html file, even though it is present in the templates subdir.
    host,ip = fetchDetails()
    return render_template("index.html",HOSTNAME=host,IP=ip)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)