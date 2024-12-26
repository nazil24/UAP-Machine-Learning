# Klasifikasi Citra Biji Kopi Berdasarkan Warna
Dataset yang digunakan bersumber dari Kaggle: https://www.google.com/url?q=https%3A%2F%2Fwww.kaggle.com%2Fdatasets%2Fgpiosenka%2Fcoffee-bean-dataset-resized-224-x-224

Proyek ini adalah implementasi klasifikasi menggunakan pendekatan Convolutional Neural Network (CNN) dan Pre-trained VGG16.

# Overview Project
Proyek ini merupakan bagian dari ujian akhir praktikum mata kuliah Machine Learning. Proyek ini berfokus pada klasifikasi citra biji kopi berdasarkan warna, dengan kategori 'Dark', 'Green', 'Light', dan 'Medium'. Sistem ini dirancang untuk membedakan jenis biji kopi yang sudah matang dan siap digunakan dari yang belum matang.

# Overview Dataset
"Biji kopi yang dipanggang dalam penelitian ini diperoleh dari JJ Mall Jatujak, di toko 'Bona Coffee.' Terdapat empat tingkat pemanggangan. Biji kopi hijau yang belum dipanggang berasal dari varietas Laos Typica Bolaven (Coffea arabica). Laos Typica Bolaven juga digunakan untuk biji kopi yang dipanggang ringan (Coffea arabica). Biji kopi Doi Chaang (Coffea arabica) digunakan untuk tingkat pemanggangan sedang, sedangkan Brazil Cerrado (Coffea arabica) digunakan untuk tingkat pemanggangan gelap.

Foto biji kopi diambil menggunakan iPhone 12 Mini dengan kamera belakang 12 megapiksel yang dilengkapi fitur Ultra-Wide dan Wide Camera. Kamera ditempatkan sejajar dengan jalur objek untuk memastikan hasil foto konsisten. Gambar biji kopi panggang diambil dalam berbagai pengaturan untuk memvalidasi variasi input gambar.

Eksperimen menggunakan pencahayaan LED dari kotak cahaya serta cahaya alami. Untuk meningkatkan noise, setiap jenis biji kopi diletakkan di dalam wadah saat difoto. Gambar dikumpulkan secara otomatis dan disimpan dalam format PNG dengan resolusi 3024x3032 piksel.

Dataset terdiri dari total 4800 foto yang diklasifikasikan ke dalam empat tingkat pemanggangan, dengan masing-masing tingkat terdiri dari 1200 foto."

# Model 
Proyek ini menggunakan model pendekatan Convolutional Neural Network (CNN) dan Pre-trained VGG16.
## *Convolutional Neural Network (CNN)*

![image](https://github.com/user-attachments/assets/f5469ea0-c65d-4786-a8a6-4352e8bae62d)

## *Pre-Trained VGG16*
![image](https://github.com/user-attachments/assets/8fe633f1-7efd-4153-bdbb-9a1cf0524b41)


# Preprocessing dan Model
## Preprocessing 
Preprocessing yang dilakukan adalah menentukan parameter gambar menggunakan h, w (224, 224), dan menentukan epoch yang digunakan yaitu 20 epoch. 

## Model dan Hasil 
Hasil dari model yang telah dibangun, sebagai berikut:
### *Convolutional Neural Network (CNN)*
![image](https://github.com/user-attachments/assets/83aa275c-71e4-4ca4-9158-2d6eda31e518)
### *Model Evaluation*
![image](https://github.com/user-attachments/assets/daec0b40-feab-467e-a540-7dd08da9d683)



