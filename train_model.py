import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

df = pd.read_csv(r"car_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Optional: print them to confirm
print("Cleaned columns:", df.columns.tolist())

# Continue processing
le_fuel = LabelEncoder()
le_trans = LabelEncoder()
df['fuel_type'] = le_fuel.fit_transform(df['fuel_type'])  # now this will work
df['transmission'] = le_trans.fit_transform(df['transmission'])

# df.rename(columns={"Kms_Driven": "mileage"}, inplace=True)
X = df[['Year', 'mileage', 'fuel_type', 'transmission', 'Owner']]
y = df['Selling_Price']
X.rename(columns={"Year": "year", "Owner": "owner"}, inplace=True)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

import joblib, os
os.makedirs("app", exist_ok=True)
joblib.dump(model, "app/car_model.pkl")
