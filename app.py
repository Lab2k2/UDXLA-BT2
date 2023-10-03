from flask import Flask, render_template, request, redirect, url_for
from controller import ImageController
import cv2
import base64
app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img_controller = ImageController(app.config['UPLOAD_FOLDER'])
            img_path = img_controller.upload_image(file)
            gray_image = img_controller.convert_to_gray(img_path)
            _, buffer = cv2.imencode('.jpg', gray_image)
            image_bytes = base64.b64encode(buffer.tobytes()).decode('utf-8')
            return render_template("result.html", image_bytes=image_bytes)
        
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

