import tkinter as tk
from tkinter import scrolledtext
from query_data import query_rag  # Ensure this function processes the chatbot's response


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LLM Chatbot")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=100, height=20)
        self.chat_area.pack(pady=10)

        self.user_input = tk.Entry(root, width=100)
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self, event=None):
        user_message = self.user_input.get()
        if user_message.strip() == "":
            return  # Don't send empty messages

        self.user_input.delete(0, tk.END)
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "You: " + user_message + "\n")
        self.chat_area.config(state='disabled')

        # Get response from the backend
        response = query_rag(user_message)

        # Display the response in the chat area
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "AI Assistant: " + response + "\n")
        self.chat_area.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
