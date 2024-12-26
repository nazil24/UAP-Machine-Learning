import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
from PIL import Image
import numpy as np
import base64

# Fungsi untuk memuat model
@st.cache_resource
def load_trained_model():
    return load_model("final_model.h5")

model = load_trained_model()

# Parameter input gambar
img_width, img_height = 224, 224  # Ukuran gambar yang sesuai dengan model

# Daftar kelas berdasarkan folder dataset
class_labels = ['Dark', 'Green', 'Light', 'Medium']

# Fungsi untuk memproses gambar sebelum prediksi
def preprocess_image(image):
    image = image.resize((img_width, img_height))  # Ubah ukuran gambar
    image = np.array(image)  # Konversi ke array numpy
    image = image / 255.0  # Normalisasi piksel
    image = np.expand_dims(image, axis=0)  # Tambahkan dimensi batch
    return image

# Fungsi untuk mendekode hasil prediksi
def decode_predictions(predictions):
    decoded = [class_labels[np.argmax(pred)] for pred in predictions]
    return decoded

# Fungsi untuk membaca gambar lokal sebagai Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Gambar lokal untuk background
local_image_path = "coffee_background.jpg"  # Nama file gambar Anda
bg_image_base64 = get_base64_of_bin_file(local_image_path)

# Konfigurasi halaman Streamlit
st.markdown(
    f"""
    <style>
    /* Mengatur background menggunakan gambar */
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    /* Mengatur warna teks menjadi hitam */
    .stMarkdown, .stTitle, .stHeader, .stSubheader, .stText {{
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Prediksi Citra Biji Kopi")
st.write("Unggah gambar untuk memprediksi menggunakan model final_model.h5.")

# Tombol untuk unggah banyak gambar
uploaded_files = st.file_uploader("Upload Gambar", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.write("Gambar yang diunggah:")
    images = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Gambar: {uploaded_file.name}", use_column_width=True)
        images.append(image)

    # Button untuk prediksi
    if st.button("Prediksi Semua Gambar"):
        st.write("Memproses dan memprediksi gambar...")

        # Proses dan prediksi semua gambar
        predictions = []
        for image in images:
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predictions.append(prediction)

        decoded_predictions = decode_predictions(predictions)

        # Tampilkan hasil prediksi
        st.write("Hasil Prediksi:")
        for i, uploaded_file in enumerate(uploaded_files):
            st.write(f"{uploaded_file.name} -> {decoded_predictions[i]}")