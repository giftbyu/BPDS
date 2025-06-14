import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# --- Konfigurasi ---
# Di kedua file .py ubah:
# Ubah MONGO_URI di kedua file menjadi:
MONGO_URI = "mongodb://admin:admin123@mongo:27017/"
DATABASE_NAME = "attrition"
COLLECTION_NAME = "employees"
CSV_FILE_PATH = "/data/model_prediction_results.csv"  # File dari hasil training

# --- Proses Pemuatan Data ---
print("Menghubungkan ke MongoDB...")
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

print(f"Memuat data prediksi dari {CSV_FILE_PATH}...")
df = pd.read_csv(CSV_FILE_PATH)

print("Menyiapkan data untuk MongoDB...")
# Konversi kolom tanggal jika ada
if 'prediction_date' in df.columns:
    df['prediction_date'] = pd.to_datetime(df['prediction_date'])

# Konversi ke dictionary
data_to_insert = df.to_dict(orient='records')

print(f"Mengimpor {len(data_to_insert)} record ke koleksi '{COLLECTION_NAME}'...")
collection.delete_many({})  # Hapus data lama
collection.insert_many(data_to_insert)

print("Update berhasil: Data prediksi atrisi telah dimuat ke MongoDB")
client.close()