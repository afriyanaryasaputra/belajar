# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan yang sudah berdiri sejak tahun 2000 memiliki reputasi yang sangat baik dan sudah mencetak banyak lulusan yang sukses. saat ini sedang menghadapi kesulitan dalam mengelola siswa, terlihat dari tingginya jumlah dropout. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Kita sebagai calon data scientist masa depan diminta untuk membuat sebuah sistem machine learning yang dapat mendeteksi siswa yang mungkin akan melakukan dropout, serta membuat sebuah business dashboard yang dapat digunakan oleh pihak Jaya Jaya Institut untuk memantau perkembangan siswa.

### Permasalahan Bisnis

Permasalahan bisnis yang akan diselesaikan melalui proyek ini antara lain:

1. Identifikasi siswa yang berpotensi melakukan dropout.
2. Memberikan bimbingan khusus kepada siswa yang berisiko dropout.
3. Memiliki sistem pemantauan perkembangan siswa untuk meningkatkan efektivitas pengelolaan.

### Cakupan Proyek

Proyek ini akan mencakup beberapa tahapan sebagai berikut:

1. Pengumpulan dan pembersihan data dari dataset Jaya Jaya Institut.
2. Pengembangan model machine learning untuk mendeteksi siswa yang berpotensi melakukan dropout.
3. Pembuatan business dashboard untuk memantau perkembangan siswa.

### Persiapan

Sumber data: [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:

1. Pastikan sudah menginstall [Anaconda](https://www.anaconda.com/products/individual) atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html) di komputer Anda.
2. Buka terminal atau command prompt.
3. Buat environment baru dengan perintah `conda create -n jaya-jaya-maju-dropout python=3.9`.
4. Aktifkan environment dengan perintah `conda activate jaya-jaya-maju-dropout`.
5. Install library yang dibutuhkan dengan perintah `pip install pandas matplotlib seaborn jupyter sqlalchemy psycopg2 scikit-learn==1.2.2 joblib==1.3.1 tensorflow streamlit`.
6. Buka Jupyter Notebook dengan perintah `jupyter-notebook .`.
7. Siap mengerjakan proyek.

## Business Dashboard

Dashboard menggunakan Tableau Public:
[Graduate Analysis Dashboard](https://public.tableau.com/views/DashboardJayaJayaInstitut/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

## Menjalankan Sistem Machine Learning

### How to run the prototype

1. Pastikan sudah menginstall streamlit di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan perintah `streamlit run app.py`.

### Online access

[Streamlit] (https://belajar-7hg4c8z3xqrpfvijtkpdpa.streamlit.app/)

## Conclusion

Berdasarkan analisis data yang telah dilakukan, dapat disimpulkan bahwa Fitur-Fitur Penting dalam Komponen Utama Pertama seperti 'Curricular_units_2nd_sem_approved' dan 'Curricular_units_2nd_sem_grade' memiliki pengaruh besar dalam menjelaskan variasi dalam data. 

### Rekomendasi Action Items

Berdasarkan hasil proyek, berikut adalah beberapa rekomendasi action items:
Perhatikan Nilai Siswa: Fitur seperti 'Curricular_units_2nd_sem_approved' dan 'Curricular_units_2nd_sem_grade' memiliki pengaruh besar dalam komponen utama pertama dan cenderung berhubungan dengan status siswa. Sehingga penting untuk memantau kemajuan siswa secara rutin, terutama di semester kedua, karena ini bisa memberikan petunjuk apakah mereka akan lulus atau tidak.

Bantu Siswa yang Kesulitan: Siswa yang mungkin menghadapi kesulitan akademik atau keuangan, seperti yang tercermin dalam fitur 'Debtor' atau 'Tuition_fees_up_to_date'. Boleh jadi, siswa butuh bantuan tambahan agar bisa lulus.

Tindak Cepat: Identifikasi siswa yang berisiko dropout lebih awal dan lakukan intervensi. Ini bisa berupa program bimbingan tambahan atau bantuan emosional untuk membantu mereka.
