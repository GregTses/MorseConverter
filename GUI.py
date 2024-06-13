from tkinter import Tk, Button, Text, Label, END
from main import play_audio, encoder, decoder


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x300')
        self.title("Morse Code Encoder/Decoder")
        self.encode_interface_on = True

        self.encode_button = Button(text="Encode", width=15, command=self.encode_interface)
        self.encode_button.place(x=180, y=25)
        self.decode_button = Button(text="Decode", width=15, command=self.decode_interface)
        self.decode_button.place(x=300, y=25)
        self.play_button = Button(text="▶", width=8, pady=14, command=self.play)
        self.play_button.place(x=513, y=198)

        self.input_label = Label(text="Text Input:", anchor="w")
        self.input_label.place(x=15, y=70)
        self.output_label = Label(text="Morse Code Output:", anchor="w")
        self.output_label.place(x=15, y=170)

        self.text_input = Text(width=70, height=3)
        self.text_input.place(x=16, y=98)
        self.text_input.bind('<KeyRelease>', self.convert)
        self.text_output = Text(width=61, height=3)
        self.text_output.place(x=16, y=198)

    def encode_interface(self):
        self.encode_interface_on = True
        self.text_output.delete('1.0', END)
        self.text_input.delete('1.0', END)
        self.input_label.config(text="Text Input:")
        self.output_label.config(text="Morse Code Output:")
        self.text_output.config(width=60)

    def decode_interface(self):
        self.encode_interface_on = False
        self.text_output.delete('1.0', END)
        self.text_input.delete('1.0', END)
        self.input_label.config(text="Morse Code Input:")
        self.output_label.config(text="Text Output:")
        self.text_output.config(width=70)

    def convert(self, event):
        self.text_output.delete('1.0', END)
        if self.encode_interface_on:
            english_text = self.text_input.get("1.0", 'end-1c')
            self.text_output.insert(END, encoder(english_text))
        else:
            morse_text = self.text_input.get("1.0", 'end-1c')
            self.text_output.insert(END, decoder(morse_text))

    def play(self):
        morse_text = self.text_output.get("1.0", 'end-1c')
        play_audio(morse_text)
