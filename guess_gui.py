import tkinter as tk
from tkinter import ttk
import pygame
import os
import random

# 🎵 Инициализируем звук
pygame.mixer.init()

def play_sound(filename):
    path = os.path.join("sounds", filename)
    pygame.mixer.Sound(path).play()

class GuessGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Угадай число")
        master.configure(bg="#eaf6ff")
        master.geometry("380x320")
        master.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=6,
                        background="#add8e6",
                        foreground="black")
        style.map("TButton",
                  background=[("active", "#87ceeb")])

        self.target = random.randint(1, 100)
        self.tries = 0

        self.label = tk.Label(master, text="Я загадал число от 1 до 100",
                              font=("Helvetica", 14), bg="#eaf6ff", fg="black")
        self.label.pack(pady=15)

        self.entry = ttk.Entry(master, font=("Helvetica", 12), justify='center')
        self.entry.pack(pady=8, ipadx=10, ipady=3)

        self.button = ttk.Button(master, text="🎯 Угадать", command=self.check_guess)
        self.button.pack(pady=10)

        self.result = tk.Label(master, text="", font=("Helvetica", 12), fg="blue", bg="#eaf6ff")
        self.result.pack(pady=10)

        self.reset_button = ttk.Button(master, text="🔄 Играть заново", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result.config(text="Пожалуйста, введи число!")
            play_sound("fail.mp3")
            return

        self.tries += 1

        if guess < self.target:
            self.result.config(text="Слишком мало!")
            play_sound("fail.mp3")
        elif guess > self.target:
            self.result.config(text="Слишком много!")
            play_sound("fail.mp3")
        else:
            self.result.config(text=f"🎉 Ты угадал число {self.target} за {self.tries} попыток!")
            play_sound("success.wav")
            time.sleep(0.8)  # 🕒 Пауза, чтобы звук успел проиграться

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.tries = 0
        self.entry.delete(0, tk.END)
        self.result.config(text="Новая игра! Попробуй снова 😉")

root = tk.Tk()
game = GuessGame(root)
root.mainloop()