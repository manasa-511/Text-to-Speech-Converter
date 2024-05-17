import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Text-to-Speech')
        self.root.geometry('400x200')  # Set window dimensions
        self.root.resizable(False, False)  # Disable window resizing

        self.label1 = tk.Label(self.root, text='Enter text to speak:', font=('Arial', 14))
        self.label1.pack(pady=10)

        self.entry = tk.Entry(self.root, font=('Arial', 12))
        self.entry.pack(ipadx=20, ipady=5)

        self.button = tk.Button(self.root, text='Speak!', command=self.clicked, font=('Arial', 12), bg='black', fg='white')
        self.button.pack(pady=10, ipadx=10, ipady=5)

        self.root.mainloop()

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

if __name__ == '__main__':
    widget = Widget()
