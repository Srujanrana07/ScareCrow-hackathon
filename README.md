# Paddy deaease Detection and Crop Recommendation System

A web-based application to detect paddy crop deaease and recommend suitable crop protection measures using a deep learning model (CNN). The application achieves high accuracy in identifying common paddy pests and suggests optimized agricultural practices to improve yield. It leverages Flask for deployment, Google Cloud Storage for model hosting, and real-time camera feed integration for instant analysis.
---

## Project Overview

This project aims to assist farmers in detecting paddy crop pests and receiving tailored crop management recommendations. By utilizing a Convolutional Neural Network (CNN), the system identifies pests from captured images and classifies them into different categories. Additionally, the system provides recommendations on pest control measures and alternative crop strategies. The trained model is deployed using Django . The web application offers an intuitive user interface, allowing users to capture images using a real-time camera feed for instant analysis and feedback.
---

![image](https://github.com/user-attachments/assets/3da53b46-8706-4465-ad0c-967ea6da45f9)
---

## 🔍 Features
- **Deep Learning Model:** A CNN trained on a diverse dataset of paddy crop pests.
- **Crop Recommendations:** Provides suitable recommendations for pest control and alternative crops.
- **Cloud Integration:** Google Cloud Storage for model hosting and easy access.
- **Web Interface:** User-friendly interface built with Flask for seamless interaction.
  
---
## 📊 Dataset Description

We provide a training dataset of **10,407 (75%)** labeled paddy leaf images across **ten classes** (nine diseases and normal leaf). Each image is accompanied by metadata, including the **paddy variety** and **age**. Your task is to develop an **accurate disease classification model** using this training dataset and classify each sample in the **test dataset of 3,469 (25%)** paddy leaf images into one of the ten categories.

---

## 📁 Files

### **1️⃣ train.csv** - The training set
- **image_id** - Unique image identifier corresponding to image file names (`.jpg`) in the `train_images` directory.
- **label** - Type of paddy disease (target class). There are ten categories, including normal leaf.
- **variety** - Name of the paddy variety.
- **age** - Age of the paddy in days.

### **2️⃣ sample_submission.csv** - Sample submission file.

### **3️⃣ train_images/** - Contains **10,407** training images stored in sub-directories corresponding to the ten target classes. File names match the `image_id` column in `train.csv`.

### **4️⃣ test_images/** - Contains **3,469** test set images.

---

## 🌾 Disease Categories

The dataset includes images categorized into the following ten classes:

1. **paddy_bacterial_leaf_blight**
2. **paddy_bacterial_leaf_streak**
3. **paddy_bacterial_panicle_blight**
4. **paddy_blast**
5. **paddy_brown_spot**
6. **paddy_dead_heart**
7. **paddy_downy_mildew**
8. **paddy_hispa**
9. **paddy_normal** (Healthy leaves)
10. **paddy_tungro**

---

## 📂 Directory Structure

```plaintext
📦 Paddy-disease-classification
Directory structure:
└── ai-hackathon-2025-scarecrow/
    ├── README.md
    ├── manage.py
    ├── requirement.txt
    ├── disease_detector/
    │   ├── _init_.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── crop_analyser.py
    │   ├── image_classifier_code.py
    │   ├── models.py
    │   ├── tempCodeRunnerFile.py
    │   ├── tests.py
    │   ├── train.py
    │   ├── views.py
    │   ├── dataset/
    │   │   └── Crop_recommendation.csv
    │   ├── migrations/
    │   │   └── _init_.py
    │   ├── model_training/
    │   │   └── crop-dataset.ipynb
    │   └── models/
    │       ├── crop_recommendation_model.pkl
    │       ├── label_encoder.pkl
    │       └── paddy_image_classifier.joblib
    ├── model_traning/
    │   └── Paddy_CNN_clasification.ipynb
    ├── scarecrowApp/
    │   ├── _init_.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── script.js
    └── templates/
        └── index.html
```
![moodelling](https://github.com/user-attachments/assets/741b00f5-facc-4cb5-8538-d2444da3b713)
---


