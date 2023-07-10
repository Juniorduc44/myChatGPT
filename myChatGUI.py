# myChatGUI v0.1.0
import customtkinter as tk
from customtkinter import CTkButton, CTkTextbox
from tkinter import messagebox, filedialog
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'


class ChatApp:
    def __init__(self, root):
        self.root = root
        openai.api_key = openai.api_key
        self.messages = [{'role': 'system', 'content': 'You are talking to GPT-3.5 assistant.'}]
        self.create_gui()

    def create_gui(self):
        self.root.title("ChatGPT GUI")

        # Text display area
        self.display_area = CTkTextbox(self.root, width=600, height=400)
        self.display_area.pack(padx=10, pady=10)

        # Text input area
        self.input_area = CTkTextbox(self.root, width=500, height=50)
        self.input_area.pack(padx=10, pady=10)

        # Send button
        self.send_button = CTkButton(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

        # Save conversation button
        self.save_button = CTkButton(self.root, text="Save Conversation", command=self.save_conversation)
        self.save_button.pack(pady=10)

    def send_message(self):
        user_message = self.input_area.get("1.0", 'end-1c')
        self.display_area.insert(tk.END, "User: " + user_message + '\n')
        self.input_area.delete('1.0', tk.END)
        self.messages.append({'role': 'user', 'content': user_message})

        # Call to the GPT-3.5 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with actual model name if different
            messages=self.messages
        )

        bot_response = response['choices'][0]['message']['content']
        self.messages.append({'role': 'assistant', 'content': bot_response})

        self.display_area.insert(tk.END, "Bot: " + bot_response + '\n')

    def save_conversation(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=(("Text file", "*.txt"),
                                                           ("All Files", "*.*")))
        if filepath:
            with open(filepath, 'w') as output_file:
                text = self.display_area.get("1.0", tk.END)
                output_file.write(text)

if __name__ == "__main__":
    root = tk.CTk()
    app = ChatApp(root)
    root.mainloop()
