import tkinter as tk
from tkinter import scrolledtext
import requests
import json
from threading import Thread

class ChatbotClient:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepSeek Chatbot nih cuyy")
        self.setup_ui()
        
        base_url = "YOUR_SERVER_URL_HERE" 
        self.server_url = base_url.rstrip('/') + '/chat'
        
    def setup_ui(self):
        # Chatdisplay
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_display.pack(padx=10, pady=10, expand=True, fill='both')
        
        # Inputframe
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=10, pady=(0, 10), fill='x')
        
        self.input_field = tk.Entry(input_frame)
        self.input_field.pack(side='left', expand=True, fill='x')
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        send_button = tk.Button(input_frame, text="Kirim", command=self.send_message)
        send_button.pack(side='right', padx=(10, 0))
        
    def send_message(self):
        message = self.input_field.get().strip()
        if not message:
            return
            
        self.input_field.delete(0, tk.END)
        self.display_message(f"Anda: {message}")
        
        Thread(target=self.send_request, args=(message,), daemon=True).start()
        
    def send_request(self, message):
        try:
            print(f"Sending request to: {self.server_url}")
            
            response = requests.post(
                self.server_url,
                json={"prompt": message},
                timeout=60,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 404:
                self.root.after(0, self.display_message, 
                    "Bot: Error: Server endpoint not found. Please check the URL configuration.")
                return
                
            response.raise_for_status()
            bot_response = response.json().get('response', 'Error: No response from server')
            self.root.after(0, self.display_message, f"Bot: {bot_response}")
            
        except requests.exceptions.ConnectionError:
            self.root.after(0, self.display_message, 
                "Bot: Error: Could not connect to server. Please check your internet connection and the server URL.")
        except requests.exceptions.Timeout:
            self.root.after(0, self.display_message, 
                "Bot: Error: Request timed out. Please try again.")
        except Exception as e:
            self.root.after(0, self.display_message, f"Bot: Error: {str(e)}")
    
    def display_message(self, message):
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotClient(root)
    root.mainloop()