# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan yang sudah berdiri sejak tahun 2000 memiliki reputasi yang sangat baik dan sudah mencetak banyak 

lulusan yang sukses. saat ini sedang menghadapi kesulitan dalam mengelola siswa, terlihat dari tingginya jumlah dropout. Oleh karena itu, Jaya Jaya Institut 

ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Kita sebagai calon data scientist masa 

depan diminta untuk membuat sebuah sistem machine learning yang dapat mendeteksi siswa yang mungkin akan melakukan dropout, serta membuat sebuah business 

dashboard yang dapat digunakan oleh pihak Jaya Jaya Institut untuk memantau perkembangan siswa.

### Permasalahan Bisnis

Permasalahan bisnis yang akan diselesaikan melalui proyek ini antara lain:

1. Temukan siswa yang mungkin akan berhenti sekolah.
2. Berikan bantuan khusus kepada siswa yang kemungkinan besar akan berhenti sekolah.
3. Pantau perkembangan siswa secara teratur untuk membuat manajemen lebih efisien.
4. Ketersediaan antarmuka web yang mudah digunakan untuk prediksi menggunakan machine learning.

### Cakupan Proyek

Proyek ini akan mencakup beberapa tahapan sebagai berikut:

1. Pengumpulan dan pembersihan data dari dataset Jaya Jaya Institut.
2. Pengembangan model machine learning untuk mendeteksi siswa yang berpotensi melakukan dropout.
3. Pembuatan business dashboard untuk memantau perkembangan siswa.
4. Pembuatan interface sederhana berbasis web untuk menggunakan sistem machine learning.


### Persiapan

Sumber data: [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:

1. Pastikan sudah menginstall [Anaconda](https://www.anaconda.com/products/individual) atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html) di 

komputer Anda.
2. Buka terminal atau command prompt.
3. Buat environment baru dengan perintah `conda create -n jaya-jaya-maju-dropout python=3.9`.
4. Aktifkan environment dengan perintah `conda activate jaya-jaya-maju-dropout`.
5. Install library yang dibutuhkan dengan perintah `pip install pandas matplotlib seaborn jupyter sqlalchemy psycopg2 scikit-learn==1.2.2 joblib==1.3.1 

tensorflow streamlit`.
6. Buka Jupyter Notebook dengan perintah `jupyter-notebook .`.
7. Siap mengerjakan proyek.

## Business Dashboard

Dashboard menggunakan Tableau Public:
[Graduate Analysis Dashboard](https://public.tableau.com/views/DashboardJayaJayaInstitut/Dashboard1?:language=en-

US&:sid=&:display_count=n&:origin=viz_share_link)

## Menjalankan Sistem Machine Learning

### How to run the prototype

1. Pastikan sudah menginstall streamlit di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan perintah `streamlit run app.py`.


### Online access

[Streamlit] (https://belajar-7hg4c8z3xqrpfvijtkpdpa.streamlit.app/)

## Conclusion

Hasil analisis PCA menunjukkan bahwa faktor-faktor yang digunakan ('Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 

'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Tuition_fees_up_to_date', 'Scholarship_holder', 'Application_mode', 'Gender', 

'Debtor', dan 'Age_at_enrollment'), memiliki pengaruh yang signifikan dalam menjelaskan struktur data. Ini menyiratkan bahwa faktor-faktor tersebut mungkin 

menjadi penentu penting dalam menentukan apakah seorang siswa akan lulus atau drop out.

Dengan memahami ini, Jaya Jaya Institut dapat menggunakan informasi dari faktor-faktor ini untuk mengambil tindakan yang sesuai guna meningkatkan tingkat 

kelulusan dan mengurangi tingkat drop out. Ini dapat meliputi pemberian dukungan tambahan, bantuan keuangan, atau program-program mentoring kepada siswa.

Jadi, kesimpulannya adalah hasil analisis PCA ini memberikan wawasan yang berharga bagi Jaya Jaya Institut untuk mengidentifikasi faktor-faktor penting yang 

memengaruhi kesuksesan akademik siswa dan mengambil langkah-langkah yang diperlukan untuk meningkatkan tingkat kelulusan mereka.

### Rekomendasi Action Items

Berdasarkan analisis PCA, Jaya Jaya Institut dapat mengambil langkah-langkah berikut:

1. Pemantauan Faktor Penting: Pantau secara aktif faktor-faktor kunci yang mempengaruhi kesuksesan siswa, seperti jumlah unit kredit, status pembayaran biaya 

kuliah, dan kepemilikan beasiswa.

2. Program Dukungan Siswa: Dirancang program dukungan tambahan seperti tutor pribadi atau konseling akademik untuk siswa yang memerlukan.

3. Bantuan Keuangan: Pertimbangkan memberikan bantuan keuangan tambahan kepada siswa yang mengalami kesulitan finansial.

4. Pengembangan Kebijakan: Kembangkan kebijakan baru untuk meningkatkan tingkat kelulusan, termasuk revisi kebijakan penerimaan siswa baru dan peningkatan layanan akademik.
