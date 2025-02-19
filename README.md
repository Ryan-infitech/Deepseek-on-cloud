<div align="right">

<a href="README.md"><img src="https://flagcdn.com/w40/gb.png" width="25"></a> | <a href="README-ID.md"><img src="https://flagcdn.com/w40/id.png" width="20"></a>

</div>

# Run DeepSeek On Cloud Computing

A semi-local chatbot implementation using DeepSeek 1.5B language model with cloud tunneling via Ngrok. This project allows you to run a powerful AI chatbot locally while making it accessible through a cloud connection. FYI you can use another model 😁

<div align=center>
<img src="https://github.com/Ryan-infitech/Deepseek-on-cloud/blob/main/Media/preview.gif?raw=true" >
</div>

## 🌟 Features

- Uses DeepSeek 1.5B language model
- Cloud tunneling with Ngrok for remote access
- Simple and intuitive GUI client
- Server-side implementation in Google Colab
- Local Python client application

## 🛠️ Requirements
<div align=center>
<img src="https://github.com/Ryan-infitech/Sistem-Absensi-Dengan-Face-Recognition/blob/main/readme/icons8-python.gif?raw=true" ><img src="https://github.com/Ryan-infitech/Sistem-Absensi-Dengan-Face-Recognition/blob/main/readme/ngrokk.gif?raw=true" ><img src="https://github.com/Ryan-infitech/Sistem-Absensi-Dengan-Face-Recognition/blob/main/readme/googlecolab.gif?raw=true" >
</div>

### Server-side (Google Colab)

- Google Colab account
- Ngrok authentication token
- Python packages:
  - flask
  - flask-cors
  - requests
  - pyngrok
  - transformers
  - accelerate

### Client-side

- Python 3.7+
- Required packages:
  - tkinter
  - requests

## 🚀 Setup Instructions

### Server Setup (Google Colab)

1. Open `server-side.ipynb` in Google Colab
2. Run the installation cells to set up dependencies
3. Replace `YOUR-NGROK-AUTH-TOKEN` with your actual Ngrok token
4. Run the server initialization cell
5. Copy the Ngrok URL provided in the output

### Client Setup

1. Open `client-side.py`
2. Replace `YOUR_SERVER_URL_HERE` with the Ngrok URL from the server
3. Run the client application:

```bash
python client-side.py
```

## 💬 Usage

1. Start the server in Google Colab
2. Launch the client application
3. Type your message in the input field
4. Press Enter or click "Kirim" to send
5. The bot will respond in the chat display

## ⚠️ Important Notes

- The Ngrok URL changes each time you restart the server
- Keep the Colab notebook running while using the chatbot
- Free Ngrok tunnels have usage limitations

## 📝 License

This project is open source and available under the MIT License.

## 👥 Contributing

Feel free to open issues and submit pull requests to improve the project.

## 🙏 Acknowledgments

- DeepSeek for their amazing language model
- Ollama for the model serving infrastructure
- Ngrok for providing the tunneling service

## 📬 Contact

[![whatsapp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6285157517798)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ryan.septiawan__)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rian-septiawan-23b0a5351/)

<br>

---

<p align="center">Made with ❤️ for fun</p>