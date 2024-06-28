import tkinter as tk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import tempfile
import os
import threading
from playsound import playsound

# Function to get language name from code
def get_language_name(code):
    return LANGUAGES[code]

# Function to speak the text using gTTS
def speak_text(text, lang_code):
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang_code, slow=False)
        
        # Create a temporary file to store the audio
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts.save(fp.name + ".mp3")
            
            # Play the audio directly from memory using playsound
            playsound(fp.name + ".mp3", block=True)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle translation
def translate_text():
    try:
        # Get input text from the text widget
        source_text = text_input.get("1.0", tk.END).strip()
        dest_language_code = lang_input.get().strip().lower()

        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Translate text to the destination language
        translator = Translator()
        translation = translator.translate(source_text, dest=dest_language_code)

        # Update the output text area with translated text and language name
        dest_language_name = get_language_name(translation.dest)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"Translated to {dest_language_name}:\n\n{translation.text}")

        # Store translated text and language for playback
        global translated_text
        translated_text = translation.text
        global translated_language
        translated_language = translation.dest

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to play translated audio
def play_translated_audio():
    global translated_text
    global translated_language
    
    if translated_text and translated_language:
        # Start a new thread for audio playback
        threading.Thread(target=speak_text, args=(translated_text, translated_language)).start()
    else:
        messagebox.showwarning("Translation Needed", "Please translate text first.")

# Setting up the GUI
root = tk.Tk()
root.title("Language Translator with Audio")
root.geometry("800x600")
root.configure(bg="#e0f7fa")

# Header
header = tk.Frame(root, bg="#00796b", height=50)
header.pack(fill=tk.X)
header_label = tk.Label(header, text="Language Translator with Audio", bg="#00796b", fg="white", font=("Arial", 24))
header_label.pack(pady=10)

# Main Content
main_frame = tk.Frame(root, bg="#e0f7fa", pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Input Section
input_frame = tk.Frame(main_frame, bg="#e0f7fa")
input_frame.pack(pady=20)

tk.Label(input_frame, text="Enter Text:", bg="#e0f7fa", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
text_input = tk.Text(input_frame, height=10, width=50, font=("Arial", 12), bd=2, relief="solid")
text_input.grid(row=1, column=0, padx=10, pady=5)

tk.Label(input_frame, text="Enter Destination Language (e.g., 'Spanish'):", bg="#e0f7fa", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
lang_input = tk.Entry(input_frame, font=("Arial", 12), bd=2, relief="solid")
lang_input.grid(row=3, column=0, padx=10, pady=5)

# Buttons Section in a Row
buttons_frame = tk.Frame(main_frame, bg="#e0f7fa")
buttons_frame.pack(pady=20)

translate_button = tk.Button(buttons_frame, text="Translate", command=translate_text, bg="#00796b", fg="white", font=("Arial", 14))
translate_button.pack(side=tk.LEFT, padx=10)

play_audio_button = tk.Button(buttons_frame, text="Play Translated Audio", command=play_translated_audio, bg="#00796b", fg="white", font=("Arial", 14))
play_audio_button.pack(side=tk.LEFT, padx=10)

# Output Section
output_frame = tk.Frame(main_frame, bg="#e0f7fa")
output_frame.pack(pady=(20, 40))  # Adding bottom margin of 40 pixels

tk.Label(output_frame, text="Translated Text:", bg="#e0f7fa", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
text_output = tk.Text(output_frame, height=10, width=50, font=("Arial", 12), bd=2, relief="solid")
text_output.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
