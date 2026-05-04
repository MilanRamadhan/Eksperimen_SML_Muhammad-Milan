# 🚢 Titanic Survival Prediction - Eksperimen SML

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk membangun model *Machine Learning* guna memprediksi keberlangsungan hidup penumpang Titanic. Model dikembangkan menggunakan **Scikit-learn**, dan seluruh proses eksperimen beserta metriknya dicatat (*tracking*) secara komprehensif menggunakan **MLflow**.

---

## 📊 Dataset
Dataset yang digunakan adalah dataset historis Titanic yang telah diproses (*data preprocessing*):
- Penanganan *missing values*
- *Feature encoding* untuk variabel kategorikal
- Fitur utama yang digunakan: `age`, `fare`, `sex`, dan lain-lain.

📁 **Lokasi File:** `dataset/dataset_clean.csv`

---

## ⚙️ Tools & Teknologi
- **Language:** Python
- **Libraries:** Scikit-learn, Pandas
- **Experiment Tracking:** MLflow
- **CI/CD:** GitHub Actions

---

## 🧠 Model & Performa
- **Algoritma:** `RandomForestClassifier` (dengan parameter *default*)
- **Akurasi Model:** **~ 76%** (`Accuracy: 0.76`)

---

## 🔁 MLflow Tracking
Semua tahapan eksperimen dicatat dalam MLflow, mencakup:
- **Parameter:** Konfigurasi *hyperparameter* model
- **Metrics:** Akurasi dan metrik evaluasi lainnya
- **Artifacts:** *Confusion Matrix*, *ROC Curve*, *Precision-Recall Curve*, dan penyimpanan model (*saved model*).

---

## 📸 Dokumentasi & Visualisasi
| MLflow Dashboard | MLflow Artifacts |
| :---: | :---: |
| ![Dashboard](Membangun_model/screenshot_dashboard.jpg) | ![Artifacts](Membangun_model/screenshot_artifak.jpg) |

---

## 🚀 Cara Menjalankan Proyek

### 1. Menjalankan Skrip Model (Lokal)
```bash
cd Membangun_model
python modelling.py
```

### 2. Membuka MLflow UI
Mulai server MLflow untuk melihat metrik dan eksperimen:
```bash
mlflow ui
```
Buka browser dan akses: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 3. Menjalankan via MLflow Project
Proyek ini sudah dikonfigurasi menggunakan format `MLProject`. Jalankan perintah berikut dari direktori utama:
```bash
mlflow run .
```

---

## 🤖 CI/CD (GitHub Actions)
Repositori ini menggunakan integrasi GitHub Actions otomatis untuk:
- Menjalankan kode `modelling.py` secara otomatis tiap kali dilakukan *push*.
- Memastikan *pipeline* Machine Learning berjalan tanpa error.

✅ **Status CI:** Berhasil (*Success*)

---

## 📁 Struktur Repositori
```text
.
├── .github/workflows/ci.yml  # Konfigurasi GitHub Actions CI/CD
├── Membangun_model/
│   ├── mlruns/               # Direktori tracking eksperimen MLflow lokal
│   ├── screenshots/          # Gambar untuk dokumentasi readme
│   ├── modelling.py          # Skrip utama pipeline ML (Training & Evaluasi)
│   └── requirements.txt      # Dependensi model
├── dataset/                  # Berisi dataset mentah dan dataset bersih
├── MLProject                 # File konfigurasi MLflow Project
├── conda.yaml                # Environment setup dependensi untuk MLflow
└── README.md                 # Dokumentasi proyek (file ini)
```

---
**👤 Author:** Muhammad Milan  
*Eksperimen Sistem Machine Learning*
