import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load Pre-Trained Model (Replace with your trained model)
model = load_model("plant_classifier.h5")  # Ensure this model exists

# Gather Farmer Input
farmer_name = input("Enter farmer's name: ")
crop_type = input("Enter planted crop type: ")
season = input("Enter the current season (e.g., summer, winter, monsoon): ")
image_path = input("Enter the image file path of the plant: ")

# Load and Display Input Image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct display

plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.axis('off')
plt.title(f"Input Image - {farmer_name}'s Crop")
plt.show()

# Preprocess Image for Prediction
img = cv2.resize(image, (224, 224))  # Resize to model input size
img = img_to_array(img) / 255.0  # Normalize pixel values
img = np.expand_dims(img, axis=0)  # Expand dimensions for model input

# Predict the Plant Name
prediction = model.predict(img)
predicted_label = np.argmax(prediction)  # Get highest probability class
plant_classes = ["Wheat", "Rice", "Maize", "Tomato", "Potato"]  # Example classes
predicted_plant = plant_classes[predicted_label]

# Display Results
print("\n🌱 **Prediction Results** 🌱")
print(f"Farmer: {farmer_name}")
print(f"Planted Crop: {crop_type}")
print(f"Season: {season}")
print(f"Predicted Plant: {predicted_plant}")