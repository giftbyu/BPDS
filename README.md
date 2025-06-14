Analisis Faktor Attrition Karyawan dan Pengembangan Dashboard HR di PT Jaya Jaya Maju

1. Business Understanding

1.1. Latar Belakang

PT Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki skala operasional yang besar dengan lebih dari 1000 karyawan di seluruh Indonesia. Sebagai perusahaan yang matang, manajemen sumber daya manusia menjadi pilar krusial untuk menjaga stabilitas dan pertumbuhan bisnis. Namun, perusahaan saat ini menghadapi tantangan signifikan terkait tingginya employee attrition rate (rasio karyawan yang keluar) yang mencapai lebih dari 10%. Angka ini dianggap tinggi untuk industri sejenis dan dapat menimbulkan dampak negatif yang serius bagi perusahaan.



1.2. Permasalahan Bisnis (Business Problem)

Tingkat atrisi yang tinggi (>10%) bukan sekadar angka statistik, melainkan representasi dari masalah fundamental yang berdampak langsung pada kinerja perusahaan. Dampak tersebut meliputi:



Biaya Rekrutmen: Biaya untuk mencari, mewawancarai, dan merekrut pengganti karyawan yang keluar.

Biaya Pelatihan: Investasi waktu dan sumber daya untuk melatih karyawan baru hingga mencapai tingkat produktivitas optimal.

Kehilangan Produktivitas: Adanya kekosongan posisi dan masa adaptasi karyawan baru menyebabkan penurunan produktivitas tim.

Kehilangan Pengetahuan Institusional: Karyawan yang lama pergi membawa serta pengetahuan dan pengalaman berharga yang tidak terdokumentasi.

Penurunan Moral Tim: Tingkat atrisi yang tinggi dapat menurunkan semangat dan loyalitas karyawan yang masih bertahan.

Manajer HR menyadari bahwa tanpa pemahaman mendalam mengenai faktor-faktor penyebabnya, upaya untuk menekan angka atrisi akan bersifat reaktif dan tidak efektif. Oleh karena itu, pertanyaan bisnis utamanya adalah:



"Apa faktor-faktor utama yang mendorong karyawan PT Jaya Jaya Maju untuk berhenti, dan bagaimana kita dapat secara proaktif mengidentifikasi karyawan yang berisiko tinggi untuk keluar?"

1.3. Tujuan Proyek (Project Goals)

Untuk menjawab permasalahan tersebut, proyek ini memiliki tiga tujuan utama:



Tujuan Analitis: Mengidentifikasi dan menganalisis faktor-faktor kunci (misalnya: demografi, kepuasan kerja, peran, kompensasi) yang memiliki korelasi terkuat dengan keputusan karyawan untuk berhenti.

Tujuan Prediktif: Membangun sebuah model machine learning yang akurat untuk memprediksi probabilitas seorang karyawan akan mengalami atrisi, sehingga memungkinkan intervensi dini.

Tujuan Operasional: Merancang sebuah business dashboard interaktif bagi manajer HR untuk memonitor metrik-metrik terkait atrisi dan faktor-faktor pendorongnya secara real-time atau periodik.

1.4. Cakupan Proyek (Project Scope)

Yang Termasuk (In-Scope):

Analisis data eksploratif pada dataset employee_data.csv.

Pra-pemrosesan data untuk persiapan pemodelan.

Pengembangan dan perbandingan 3 model klasifikasi: Regresi Logistik (sebagai pengganti Regresi Linear yang tidak sesuai untuk masalah klasifikasi), Random Forest, dan XGBoost.

Analisis dampak teknik oversampling SMOTE pada performa model.

Interpretasi hasil model untuk mengidentifikasi faktor-faktor paling berpengaruh.

Penyusunan kerangka dan desain untuk business dashboard.

Yang Tidak Termasuk (Out-of-Scope):

Pengumpulan data baru dari sumber lain (misalnya: survei lanjutan, data absensi).

Implementasi live dashboard ke dalam sistem produksi perusahaan.

Pengembangan dan implementasi kebijakan HR baru berdasarkan hasil analisis (proyek ini hanya memberikan rekomendasi berbasis data).

2. Rencana Program dan Tahapan Proyek

Berikut adalah program kerja yang akan dijalankan, dari analisis data hingga evaluasi model.



Tahap 1: Pemahaman Data dan Analisis Data Eksploratif (EDA)

Langkah awal adalah memahami dataset yang ada.



Memuat Data: Mengimpor employee_data.csv ke dalam lingkungan analisis.

Statistik Deskriptif: Melihat ringkasan statistik (rata-rata, median, standar deviasi) untuk fitur numerik.

Pemeriksaan Kualitas Data: Mengecek nilai yang hilang (missing values) dan duplikasi data.

Visualisasi Data:Melihat distribusi variabel target (Attrition) untuk mengonfirmasi adanya ketidakseimbangan kelas (imbalanced data).

Membuat histogram dan box plot untuk fitur numerik (misalnya: MonthlyIncome, Age).

Membuat bar chart untuk fitur kategorikal (misalnya: Department, Gender, JobSatisfaction).

Menganalisis hubungan antara setiap fitur dengan Attrition (misalnya: tingkat atrisi per departemen, perbandingan pendapatan antara karyawan yang bertahan dan yang keluar).

Tahap 2: Pra-pemrosesan Data (Data Preprocessing)

Menyiapkan data agar siap digunakan untuk pemodelan.



Encoding Variabel Kategorikal: Mengubah variabel non-numerik (seperti Department, Gender) menjadi format numerik menggunakan teknik seperti One-Hot Encoding.

Pemisahan Data: Memisahkan dataset menjadi fitur (X) dan target (y, yaitu Attrition).

Pembagian Train-Test: Membagi data menjadi data latih (training set) dan data uji (testing set) dengan proporsi tertentu (misalnya, 80:20). Ini penting untuk mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.

Penskalaan Fitur (Feature Scaling): Menyamakan skala fitur-fitur numerik menggunakan StandardScaler agar model seperti Regresi Logistik dapat bekerja optimal.

Tahap 3: Pemodelan Machine Learning

Proses ini akan dibagi menjadi dua skenario utama.

Koreksi Penting: Permintaan awal menyebutkan Linear Regression. Namun, Linear Regression digunakan untuk memprediksi nilai kontinu (misalnya, harga rumah). Karena target kita adalah Attrition (Ya/Tidak), ini adalah masalah klasifikasi. Model linear yang tepat untuk ini adalah Regresi Logistik (Logistic Regression). Saya akan menggunakan model ini sebagai perwakilan model linear.



Skenario 1: Pemodelan Sebelum SMOTE (Data Imbalanced)

Melatih model Regresi Logistik, Random Forest, dan XGBoost pada training set yang asli (imbalanced).

Melakukan prediksi pada testing set.

Mengevaluasi performa masing-masing model.

Skenario 2: Pemodelan Sesudah SMOTE (Data Balanced)

Menerapkan SMOTE (Synthetic Minority Over-sampling Technique) pada training set. Penting: SMOTE hanya diterapkan pada data latih untuk mencegah kebocoran data (data leakage).

Melatih kembali model Regresi Logistik, Random Forest, dan XGBoost pada training set yang sudah seimbang.

Melakukan prediksi pada testing set yang asli (imbalanced).

Mengevaluasi performa masing-masing model.

Tahap 4: Evaluasi Model

Karena data tidak seimbang, akurasi saja tidak cukup. Metrik evaluasi yang akan digunakan adalah:



Accuracy: Persentase prediksi yang benar secara keseluruhan.

Precision: Dari semua yang diprediksi "Ya" (akan keluar), berapa persen yang benar-benar keluar. Penting untuk tidak salah menuduh karyawan akan keluar.

Recall (Sensitivity): Dari semua karyawan yang sebenarnya keluar, berapa persen yang berhasil diprediksi oleh model. Penting untuk menangkap sebanyak mungkin kasus atrisi.

F1-Score: Rata-rata harmonik dari Precision dan Recall, memberikan gambaran seimbang.

AUC-ROC: Kemampuan model untuk membedakan antara kelas positif dan negatif.

Hasil dari keenam model (3 model x 2 skenario) akan disajikan dalam tabel perbandingan untuk menentukan model terbaik. Selain itu, akan dianalisis fitur-fitur yang paling berpengaruh (feature importance) dari model terbaik (biasanya Random Forest atau XGBoost).



Tahap 5: Desain Business Dashboard

Berdasarkan temuan dari analisis dan model, sebuah desain dashboard akan diusulkan. Isinya mencakup:



Key Performance Indicators (KPIs):Tingkat Atrisi Keseluruhan (%).

Jumlah Karyawan Keluar (bulan ini/kuartal ini).

Tingkat Atrisi per Departemen.

Visualisasi Faktor Utama:Grafik batang: Atrisi berdasarkan Tingkat Kepuasan Kerja (JobSatisfaction), Lingkungan Kerja (EnvironmentSatisfaction).

Box plot: Distribusi Gaji Bulanan (MonthlyIncome) untuk karyawan yang bertahan vs. keluar.

Grafik: Tingkat Atrisi berdasarkan Lama Bekerja (YearsAtCompany).

Filter Interaktif:Kemampuan untuk memfilter data berdasarkan Departemen, Peran Pekerjaan, Tingkat Jabatan, dan Rentang Usia untuk analisis yang lebih mendalam.

(Opsional) Watchlist Karyawan:Daftar karyawan yang diprediksi oleh model memiliki risiko atrisi tertinggi, memungkinkan HR untuk melakukan intervensi proaktif.

