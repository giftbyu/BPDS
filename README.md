# Proyek Analisis: Mengatasi Attrition Karyawan di PT Jaya Jaya Maju

## Business Understanding

### Latar Belakang
PT Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan skala operasional yang besar mencakup lebih dari 1.000 karyawan di seluruh Indonesia. Sebagai perusahaan yang matang, stabilitas sumber daya manusia menjadi pilar krusial bagi pertumbuhan bisnis.

Namun, saat ini perusahaan menghadapi tantangan signifikan terkait tingginya *employee attrition rate* (rasio karyawan keluar) yang telah mencapai lebih dari **10%**. Angka ini dianggap tinggi untuk industri sejenis dan berpotensi menimbulkan dampak negatif yang serius, seperti:

* **Peningkatan Biaya:** Biaya rekrutmen dan pelatihan untuk menggantikan karyawan yang keluar terus meningkat.
* **Kehilangan Produktivitas:** Adanya kekosongan posisi dan masa adaptasi karyawan baru menyebabkan penurunan produktivitas tim secara keseluruhan.
* **Hilangnya Pengetahuan Institusional:** Karyawan senior yang pergi membawa serta pengetahuan dan pengalaman berharga yang tidak terdokumentasi.
* **Penurunan Moral Tim:** Tingkat atrisi yang tinggi dapat menurunkan semangat dan loyalitas karyawan yang masih bertahan.

Manajemen HR menyadari bahwa tanpa pemahaman mendalam mengenai faktor penyebabnya, upaya untuk menekan angka atrisi akan bersifat reaktif dan tidak efektif.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan adalah tingginya tingkat atrisi yang berdampak langsung pada kinerja perusahaan. Oleh karena itu, pertanyaan bisnis yang menjadi fokus proyek ini adalah:

> **"Apa faktor-faktor utama yang mendorong karyawan PT Jaya Jaya Maju untuk berhenti, dan bagaimana kita dapat secara proaktif mengidentifikasi karyawan yang berisiko tinggi untuk keluar?"**

Untuk menjawabnya, proyek ini memiliki tiga tujuan utama:
1.  **Analitis:** Mengidentifikasi dan menganalisis faktor-faktor kunci (seperti demografi, kepuasan kerja, peran, dan kompensasi) yang memiliki korelasi terkuat dengan keputusan karyawan untuk berhenti.
2.  **Prediktif:** Membangun model *machine learning* yang akurat untuk memprediksi probabilitas seorang karyawan akan mengalami atrisi, sehingga memungkinkan intervensi dini.
3.  **Operasional:** Merancang sebuah *business dashboard* interaktif bagi manajer HR untuk memonitor metrik-metrik terkait atrisi dan faktor pendorongnya secara periodik.

## Cakupan Proyek
Proyek ini mencakup beberapa tahapan utama, antara lain:
* **Analisis Data Eksploratif:** Melakukan analisis mendalam pada dataset `employee_data.csv` untuk menemukan pola dan wawasan awal.
* **Pra-pemrosesan Data:** Menyiapkan data agar siap untuk pemodelan, termasuk *encoding* dan *scaling*.
* **Pengembangan Model Klasifikasi:** Mengembangkan dan membandingkan 3 model klasifikasi: `Regresi Logistik`, `Random Forest`, dan `XGBoost`.
* **Analisis Dampak SMOTE:** Menganalisis pengaruh teknik *oversampling* (`SMOTE`) untuk menangani data yang tidak seimbang.
* **Interpretasi Hasil Model:** Mengidentifikasi faktor-faktor paling berpengaruh berdasarkan model dengan performa terbaik.
* **Penyusunan Desain Dashboard:** Merancang kerangka dan desain untuk *business dashboard* di Metabase.

## Pendekatan Analisis dan Pemodelan

Proyek ini menggunakan pendekatan kuantitatif yang terstruktur, dimulai dari analisis data hingga evaluasi model.

1.  **Pemahaman Data (EDA):** Statistik deskriptif dan visualisasi (histogram, *box plot*, *bar chart*) digunakan untuk memahami distribusi data dan hubungan antar variabel dengan `Attrition`.
2.  **Pra-pemrosesan Data:** Variabel kategorikal diubah menggunakan *One-Hot Encoding*, dan fitur numerik diskalakan dengan `StandardScaler` untuk mengoptimalkan performa model.
3.  **Pemodelan Machine Learning:** Dilakukan dua skenario pemodelan:
    * **Skenario 1:** Melatih model pada data asli yang tidak seimbang (*imbalanced*).
    * **Skenario 2:** Melatih model pada data yang telah diseimbangkan menggunakan `SMOTE`.
4.  **Evaluasi Model:** Performa model diukur menggunakan metrik yang komprehensif seperti `Accuracy`, `Precision`, `Recall`, `F1-Score`, dan `AUC-ROC` untuk mendapatkan gambaran yang akurat pada data yang tidak seimbang.

## Business Dashboard

Berdasarkan temuan dari analisis dan model, sebuah desain *dashboard* interaktif diusulkan untuk membantu manajer HR. Isinya mencakup:

* **Key Performance Indicators (KPIs):**
    * Tingkat Atrisi Keseluruhan (%).
    * Jumlah Karyawan Keluar.
    * Tingkat Atrisi per Departemen.
* **Visualisasi Faktor Utama:**
    * Grafik batang atrisi berdasarkan `JobSatisfaction`.
    * *Bor* untuk distribusi `MonthlyIncome` antara karyawan yang bertahan vs. keluar.
    * Grafik tren atrisi berdasarkan `YearsAtCompany`.
* **Filter Interaktif:**
    * Kemampuan untuk memfilter data berdasarkan `Departemen`, `Peran Pekerjaan`, `Tingkat Jabatan`, dan `Rentang Usia` untuk analisis yang lebih mendalam.
* **Watchlist Karyawan (Proaktif):**
    * Daftar karyawan yang diprediksi oleh model memiliki risiko atrisi tertinggi, memungkinkan HR untuk melakukan intervensi secara proaktif.

## Kesimpulan dan Rekomendasi

Proyek ini berhasil mengidentifikasi faktor-faktor kunci penyebab atrisi dan membangun kerangka kerja untuk memprediksi serta memonitornya. Model *machine learning* yang dikembangkan dapat menjadi aset berharga bagi perusahaan untuk mengambil keputusan berbasis data.

**Rekomendasi Aksi untuk Perusahaan:**

* **Fokus pada Faktor Pendorong Utama:** Berdasarkan hasil analisis, perusahaan disarankan untuk meninjau kebijakan terkait faktor-faktor yang paling berpengaruh, seperti kompensasi (`MonthlyIncome`), beban kerja (`OverTime`), dan jenjang karir (`JobLevel`).
* **Gunakan Dashboard untuk Intervensi Dini:** Manajer HR harus secara aktif menggunakan "Watchlist Karyawan" pada *dashboard* untuk mendekati karyawan yang berisiko tinggi, memahami masalah mereka, dan menawarkan solusi sebelum mereka memutuskan untuk keluar.
* **Program Retensi Berbasis Segmen:** Dengan menggunakan filter pada *dashboard*, HR dapat merancang program retensi yang lebih spesifik untuk departemen, peran, atau kelompok karyawan dengan tingkat atrisi tertinggi.
