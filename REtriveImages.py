from flask import Flask, request, jsonify
import base64
import os
from flask_cors import CORS
from flask import Flask, send_from_directory
import pickle
import random

# Load the filename list
with open('filename_list.pkl', 'rb') as f:
    filename = pickle.load(f)
new_prefix = "C:/Users/91701/Downloads/archive (24)/outfit_items_dataset/"

# Modify the filenames
filename = [filename.replace("/kaggle/input/fashionoutfititems/outfit_items_dataset/", new_prefix) for filename in filename]


app = Flask(__name__)
print("filename 56",filename[0])
CORS(app)
@app.route("/getimageswithid",methods=['POST'])
def getid():
        
        try:
            data=request.get_json()
            data=data.get('ids')
           
            similar_image_paths=[]
            if isinstance(data, list) and all(isinstance(item, list) for item in data):
                for array in data:
                    for y in array:
                        similar_image_path = filename[y]
                        similar_image_paths.append(similar_image_path)
            
            elif isinstance(data, list):
                for y in data:
                    similar_image_path = filename[y]
                    similar_image_paths.append(similar_image_path)
            

            images = []
            for path in similar_image_paths:
                print("path is ", path)
                try:
                    
                    path_parts = path.split("/")

                    # Extract text after the 6th and 7th slash
                    if len(path_parts) >= 8:
                        after_6th_slash = path_parts[6]
                        after_7th_slash = path_parts[7]
                        combined_text = f"{after_6th_slash}-{after_7th_slash}"
                except Exception as e:
                     print(f"Error processing image path '{path}': {e}")
                
                with open(path, "rb") as f:
                    image_data = base64.b64encode(f.read()).decode('utf-8')
                    images.append({'image_data': image_data, 'combined_text': combined_text})
                    
                
           
            return jsonify(images=images)

                 
        except Exception as e:
              print('Error uploading image:', str(e))
              return 'Internal server error', 500
        

@app.route("/newproducts",methods=['GET']) 
def new_products():
    
    similar_image_paths=[]
    images=[]
    for i in range(10):
       id=random.randint(1,40000)
       similar_image_path=filename[id]
       similar_image_paths.append(similar_image_path)
    for path in similar_image_paths:
        print("path is ", path)
        try:
            
            path_parts = path.split("/")

            # Extract text after the 6th and 7th slash
            if len(path_parts) >= 8:
                after_6th_slash = path_parts[6]
                after_7th_slash = path_parts[7]
                combined_text = f"{after_6th_slash}-{after_7th_slash}"
        except Exception as e:
                print(f"Error processing image path '{path}': {e}")
        
        with open(path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
            images.append({'image_data': image_data, 'combined_text': combined_text})
            
        
    
    return jsonify(images=images)




    


    
    


  

if __name__ == '__main__':
    app.run(debug=False,port=5001)