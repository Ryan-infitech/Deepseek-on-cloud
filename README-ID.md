<div align="right">

<a href="README.md"><img src="https://flagcdn.com/w40/gb.png" width="25"></a> | <a href="README-ID.md"><img src="https://flagcdn.com/w40/id.png" width="20"></a>

</div>

# Jalanin Deepseek Di Cloud Buat PC Kentang :v

Implementasi chatbot semi-lokal menggunakan model bahasa DeepSeek 1.5B dengan terowongan cloud melalui Ngrok. Proyek ini memungkinkan Anda menjalankan chatbot AI yang powerful secara lokal sambil membuatnya dapat diakses melalui koneksi cloud. FYI Anda bisa menggunakan model lain 😁

<div align=center>
<img src="https://github.com/Ryan-infitech/Deepseek-on-cloud/blob/main/Media/preview.gif?raw=true" >
</div>

## 🌟 Fitur

- Menggunakan model bahasa DeepSeek 1.5B
- Terowongan cloud dengan Ngrok untuk akses jarak jauh
- Antarmuka pengguna GUI yang sederhana dan intuitif
- Implementasi server di Google Colab
- Aplikasi klien Python lokal

## 🛠️ Persyaratan

### Sisi Server (Google Colab)

- Akun Google Colab
- Token autentikasi Ngrok
- Paket Python:
  - flask
  - flask-cors
  - requests
  - pyngrok
  - transformers
  - accelerate

### Sisi Klien

- Python 3.7+
- Paket yang diperlukan:
  - tkinter
  - requests

## 🚀 Petunjuk Pengaturan

### Pengaturan Server (Google Colab)

1. Buka `server-side.ipynb` di Google Colab
2. Jalankan sel instalasi untuk mengatur dependensi
3. Ganti `YOUR-NGROK-AUTH-TOKEN` dengan token Ngrok Anda yang sebenarnya
4. Jalankan sel inisialisasi server
5. Salin URL Ngrok yang diberikan dalam output

### Pengaturan Klien

1. Buka `client-side.py`
2. Ganti `YOUR_SERVER_URL_HERE` dengan URL Ngrok dari server
3. Jalankan aplikasi klien:

```bash
python client-side.py
```

## 💬 Cara Penggunaan

1. Mulai server di Google Colab
2. Jalankan aplikasi klien
3. Ketik pesan Anda di kolom input
4. Tekan Enter atau klik "Kirim" untuk mengirim
5. Bot akan merespons di tampilan chat

## ⚠️ Catatan Penting

- URL Ngrok berubah setiap kali Anda me-restart server
- Jaga agar notebook Colab tetap berjalan saat menggunakan chatbot
- Terowongan Ngrok gratis memiliki batasan penggunaan

## 📝 Lisensi

Proyek ini bersifat open source dan tersedia di bawah Lisensi MIT.

## 👥 Berkontribusi

Jangan ragu untuk membuka issues dan mengajukan pull request untuk meningkatkan proyek.

## 🙏 Ucapan Terima Kasih

- DeepSeek untuk model bahasa mereka yang luar biasa
- Ollama untuk infrastruktur serving model
- Ngrok untuk menyediakan layanan terowongan

## 📬 Kontak

[![whatsapp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6285157517798)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ryan.septiawan__)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rian-septiawan-23b0a5351/)

<br>

---

<p align="center">Made with ❤️ for fun</p>
