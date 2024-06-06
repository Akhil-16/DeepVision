from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from keras.models import load_model,Model
import ultralytics
from ultralytics import YOLO
from keras.applications.resnet50 import ResNet50
from keras.layers import GlobalAveragePooling2D


app = Flask(__name__)
CORS(app)

# Load pre-calculated feature array
feature_array = np.load("C:/Project-3/features.npy")
print("feature array is ",feature_array[205])

# Load pre-trained ResNet50 model as feature extractor
# feature_extractor_model = load_model("feature_extractor_model.h5")
resnet_model = ResNet50(weights = 'imagenet' ,include_top = False, input_shape=(224,224,3))
resnet_model.trainable=False
x = resnet_model.output
x = GlobalAveragePooling2D()(x)
feature_extractor_model = Model(inputs=resnet_model.input, outputs=x)


@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'photo' not in request.files:
            return 'No file part', 400
        
        file = request.files['photo']
        if file.filename == '':
            return 'No selected file', 400

        # Read image file
        image_data = file.read()
        nparr = np.frombuffer(image_data, np.uint8)
        image_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Initialize YOLO model
        yolo_model = YOLO("fashionbest.pt")
        results = yolo_model(image_np)
        boxes = results[0].boxes.xyxy.tolist()

        if len(boxes)==0:
            rs_img=cv2.resize(image_np, (224,224))
            preprocessed_image = preprocess_input(rs_img)
            preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
            features=feature_extractor_model.predict(preprocessed_image)
            result = features.flatten()
            normalized = result / np.linalg.norm(result)
            print("features are ",normalized)

            # Calculate cosine similarity
            similarities = cosine_similarity(normalized.reshape(1, -1), feature_array)
            similar_indices = np.argsort(similarities[0])[::-1]
            top_5 = similar_indices[1:20].tolist()
            return jsonify({'top_5': top_5})
            







        base_filename = "cropped_object_"
        all_top_5 = []

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = box

            # Crop the object using bounding box coordinates
            cropped_object = image_np[int(y1):int(y2), int(x1):int(x2)]
            
            # Resize and preprocess cropped object
            new_img = cv2.resize(cropped_object, (224, 224))
            
            img_array = np.array(new_img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Extract features using pre-trained ResNet50 model
            features = feature_extractor_model.predict(img_array)
           
            result = features.flatten()
            normalized = result / np.linalg.norm(result)
            print("features are ",normalized)

            # Calculate cosine similarity
            similarities = cosine_similarity(normalized.reshape(1, -1), feature_array)
            similar_indices = np.argsort(similarities[0])[::-1]
            top_5 = similar_indices[:5].tolist()
            all_top_5.append(top_5)

            # Save cropped object
            unique_filename = f"{base_filename}{i:03d}.jpg"
            cv2.imwrite(unique_filename, new_img)

        print("Cropped objects saved successfully!")
        print("All top_5 indices are", all_top_5)

        return jsonify({'top_5': all_top_5})
    
    except Exception as e:
        print('Error uploading image:', str(e))
        return 'Internal server error', 500

if __name__ == '__main__':
    app.run(debug=False)
