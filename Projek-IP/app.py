from flask import Flask, render_template, request
from subnet import kalkulator_subnet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None

    if request.method == "POST":
        try:
            ip_input = request.form["ip"]
            prefix = request.form.get("prefix")
            prefix = int(prefix) if prefix else None
            hasil = kalkulator_subnet(ip_input, prefix)
        except Exception as e:
            error = str(e)

    return render_template("index.html", hasil=hasil, error=error)

if __name__ == "__main__":
    app.run