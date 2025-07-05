
# 🚗 Car Price Prediction API

A FastAPI-based machine learning API that predicts used car prices based on input features such as year, mileage, fuel type, transmission type, and owner count.

This project is containerized with Docker and deployed on Hugging Face Spaces.

---

## 📦 Features

- 🔮 Predicts car resale price using a trained Random Forest model
- ⚡ Built with FastAPI
- 🐳 Dockerized
- 🌐 Deployed on Hugging Face Spaces
- 🧪 Interactive Swagger docs for testing

---

## 🧠 Model Input Format

```json
{
  "year": 2017,
  "mileage": 45000,
  "fuel_type": 0,
  "transmission": 1,
  "owner": 0
}
```

- `fuel_type`: 0 = Petrol, 1 = Diesel, 2 = CNG
- `transmission`: 0 = Manual, 1 = Automatic
- `owner`: 0 = First owner, 1 = Second owner, etc.

---

## 🚀 Try It Live

👉 [**Open API Docs**](https://prathikbs-car-price-api.hf.space/docs)  
Use the `/predict` endpoint to submit input and get the predicted selling price.

---

## 🛠️ Tech Stack

- Python 3.10
- FastAPI
- scikit-learn
- Pandas
- Uvicorn
- Docker

---

## 📂 Project Structure

```
car-price-api/
├── app/
│   ├── main.py         # FastAPI app & route
│   ├── model.py        # Pydantic input schema
│   └── car_model.pkl   # Trained ML model
├── train_model.py      # Trains and dumps model
├── requirements.txt    # Python dependencies
├── Dockerfile          # Hugging Face-compatible image
└── README.md
```

---

## 🐳 Run Locally

```bash
git clone https://github.com/prathikbsgowda/car-price-api.git
cd car-price-api

# Optional: create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Train model
python train_model.py

# Run FastAPI app
uvicorn app.main:app --reload
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test.

---

## ✨ Deployed On

[![Hugging Face Spaces](https://img.shields.io/badge/hosted%20on-HuggingFace-orange?logo=huggingface)]([https://huggingface.co/spaces/prathikbs/car-price-api](https://prathikbs-car-price-api.hf.space/docs))

---

## 📬 Contact

Created by **Prathik B S Gowda**  
📧 prathikbsgowda@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/prathik-b-s-a80b3521a)
