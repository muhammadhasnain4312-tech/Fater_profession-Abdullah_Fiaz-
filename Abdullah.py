# Farmer Dad Chatbot using Python Tkinter
# Father's Profession: Farmer

import tkinter as tk

# Farmer Q&A Database
qa = {
    "what is your profession": "I am a farmer. 🌾",
    "what do you do": "I grow crops and take care of my farm.",
    "what crops do you grow": "I grow wheat, rice, vegetables, and mustard.",
    "how much do you earn": "My income depends on crop production and market prices.",
    "do you like farming": "Yes, I love farming. It is my passion.",
    "what is your daily routine": "I wake up early, visit fields, irrigate crops, and manage farm work.",
    "can a farmer get promotion": "A farmer cannot get a job promotion, but can expand land and use modern technology.",
    "what is your goal": "My goal is to become a progressive farmer.",
    "do you use technology": "Yes, I use tractors, irrigation systems, and mobile apps.",
    "what is your farm size": "I have about 5 acres of farmland.",
    "who are you": "I am your farmer father chatbot.",
    "hello": "Hello! I am Farmer Dad. Ask me anything about farming.",
    "hi": "Hi! How can I help you today?",
    "bye": "Goodbye! Have a great day."
}

# Chat Function
def send_message():
    user_msg = entry.get().lower().strip()

    if user_msg == "":
        return

    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    response = qa.get(
        user_msg,
        "Sorry, I don't know the answer to that question."
    )

    chat_area.insert(tk.END, "Farmer Dad: " + response + "\n\n")

    entry.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("🌾 Farmer Dad Chatbot 🌾")
root.geometry("600x500")

title = tk.Label(
    root,
    text="🌾 Farmer Dad Chatbot 🌾",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

chat_area = tk.Text(root, height=20, width=70)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_btn = tk.Button(
    root,
    text="Send",
    command=send_message
)
send_btn.pack(side=tk.LEFT)

root.mainloop()
