from flask import Flask, render_template, request, send_from_directory
import os
from faceprofiling import analyze_face

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", error="No file uploaded")

        file = request.files["image"]
        if file.filename == "":
            return render_template("index.html", error="No selected file")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Analyze face
        results = analyze_face(filepath)

        return render_template("index.html", results=results)

    return render_template("index.html", results=None)

@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
