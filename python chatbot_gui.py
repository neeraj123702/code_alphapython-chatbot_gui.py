import tkinter as tk

def get_bot_reply(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def send_message():
    user_msg = user_entry.get()
    if user_msg.strip() == "":
        return

    chat_text.insert(tk.END, "You: " + user_msg + "\n")
    bot_reply = get_bot_reply(user_msg)
    chat_text.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("🤖 Simple Chatbot")

chat_text = tk.Text(root, height=20, width=50, state="normal")
chat_text.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

root.mainloop()
