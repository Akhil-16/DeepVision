from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'photo' not in request.files:
        return 'No file uploaded', 400

    file = request.files['photo']
    if file.filename == '':
        return 'No selected file', 400

    try:
        # Read the image file
        img = Image.open(io.BytesIO(file.read()))
        # Do something with the image (e.g., save it to disk)
        img.save('uploaded_image.jpg')  # Save the image to disk (you can modify the filename/path)

        return 'Image uploaded successfully'
    except Exception as e:
        return f'Error processing image: {str(e)}', 500

@app.route('/display', methods=['GET'])
def display_image():
    try:
        # Send the image file back to the client
        return send_file('uploaded_image.jpg', mimetype='image/jpeg')
    except Exception as e:
        return f'Error displaying image: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
