from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        source = source_lang.get()
        target = target_lang.get()

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, str(e))


# Main Window
root = Tk()
root.title("Language Translator")
root.geometry("700x500")

# Language list
languages = [
    "english",
    "hindi",
    "telugu",
    "tamil",
    "french",
    "german",
    "spanish",
    "japanese",
    "korean",
    "arabic"
]

# Heading
Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Input Label
Label(root, text="Enter Text").pack()

# Input Text Box
input_text = Text(root, height=6, width=60)
input_text.pack(pady=5)

# Source Language
Label(root, text="Source Language").pack()

source_lang = ttk.Combobox(root, values=languages)
source_lang.pack()
source_lang.set("english")

# Target Language
Label(root, text="Target Language").pack()

target_lang = ttk.Combobox(root, values=languages)
target_lang.pack()
target_lang.set("hindi")

# Translate Button
Button(
    root,
    text="Translate",
    command=translate_text,
    bg="green",
    fg="white"
).pack(pady=10)

# Output Label
Label(root, text="Translated Text").pack()

# Output Text Box
output_text = Text(root, height=6, width=60)
output_text.pack(pady=5)

root.mainloop()