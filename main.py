import re
from playsound import playsound
from GUI import *
from data import MORSE_TO_TEXT, TEXT_TO_MORSE


def encoder(english_text):
    english_text = re.sub(r"\s+", " ", english_text).upper()
    encoded_text = ""
    for char in english_text:
        try:
            encoded_text += TEXT_TO_MORSE[char] + " "
        except KeyError:
            return "Invalid character"
    return encoded_text[:-1]


def decoder(morse_text):
    morse_text = re.sub(r"\s+", " ", morse_text)
    morse_list = morse_text.split(" ")
    decoded_text = ""
    for i in morse_list:
        try:
            decoded_text += MORSE_TO_TEXT[i]
        except KeyError:
            return "Invalid character"
    return decoded_text


def play_audio(morse_text):
    for char in morse_text:
        playsound("Sounds/DotSilence.mp3")
        match char:
            case ".":
                playsound("Sounds/Dot.mp3")
            case "-":
                playsound("Sounds/Dash.mp3")
            case "/":
                playsound("Sounds/DotSilence.mp3")
            case _:
                playsound("Sounds/DotSilence.mp3")
                playsound("Sounds/DotSilence.mp3")


if __name__ == "__main__":
    app = Window()
    app.mainloop()

