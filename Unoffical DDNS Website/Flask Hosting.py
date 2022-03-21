from flask import Flask, redirect, url_for, render_template
import os, socket

app = Flask(__name__, static_url_path='/static')

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return "Up"
    except:
        return "Down"
    finally:
        s.close()

@app.route("/")
def home():
    b1 = isOpen("mindustry.ddns.net", 1000)
    b2 = isOpen("mindustry.ddns.net", 2000)
    b3 = isOpen("mindustry.ddns.net", 3000)
    b4 = isOpen("mindustry.ddns.net", 4000)
    return render_template("index.html", a1=b1, a2=b2, a3=b3, a4=b4)
@app.route("/ourstaff")
def ourstaff():
    return render_template("our-staff.html")
@app.route("/common-issues-and-fixes")
def ciaf():
    return render_template("commonIssuesAndFixes.html")

@app.route("/iconee")
def iconee():
    return render_template("iconee.html")


if __name__ == "__main__":
    app.run(debug=True)