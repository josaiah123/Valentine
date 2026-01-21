import tkinter as tk
from PIL import Image, ImageTk
import pygame

# ================= SETTINGS =================
MY_NAME = "Josaiah"
HER_NAME = "Ibaba"
PHOTO_FILE = "photo.jpeg"
MUSIC_FILE = "music.mp3"

BG = "#FFE4E1"
CARD = "#FFF8F6"
TEXT = "#7A0000"
ACCENT = "#FF2E93"

# ================= MUSIC =================
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILE)
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play(-1)

# ================= WINDOW =================
root = tk.Tk()
root.title(f"For {HER_NAME} ❤️ From {MY_NAME}")
root.geometry("1200x750")
root.configure(bg=BG)

# ================= CARD =================
card = tk.Frame(root, bg=CARD)
card.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=550)

# ================= PHOTO =================
img = Image.open(PHOTO_FILE).resize((320, 320), Image.Resampling.LANCZOS)
photo_img = ImageTk.PhotoImage(img)

tk.Label(
    card,
    image=photo_img,
    bg=CARD,
    bd=4,
    relief="ridge"
).place(x=80, y=100)

# ================= LETTER =================
letter_text = (
    f"Dear {HER_NAME},\n\n"
    "From the very first moment I saw you,\n"
    "I knew my heart had finally found its home.\n\n"
    "You mean more to me than words can ever say.\n\n"
    "Will you be my Valentine?\n\n"
    f"With love,\n"
    f"{MY_NAME}"
)

letter = tk.Label(
    card,
    text=letter_text,
    bg=CARD,
    fg=TEXT,
    font=("Segoe Script", 20),
    justify="left",
    wraplength=500
)
letter.place(x=460, y=90)

# ================= BUTTON AREA =================
btn_area = tk.Frame(card, bg=CARD)
btn_area.place(x=460, y=420, width=500, height=80)


def yes_clicked():
    card.destroy()
    tk.Label(
        root,
        text="You just made my heart smile ❤️\n\nHappy Valentine’s Day",
        bg=BG,
        fg=TEXT,
        font=("Segoe Script", 36),
        justify="center"
    ).pack(expand=True)


yes_btn = tk.Button(
    btn_area,
    text="YES 💖",
    bg=ACCENT,
    fg="white",
    font=("Comic Sans MS", 24, "bold"),
    padx=30,
    pady=10,
    command=yes_clicked
)
yes_btn.place(x=40, y=10)

no_btn = tk.Button(
    btn_area,
    text="NO 😢",
    bg="#8B0000",
    fg="white",
    font=("Comic Sans MS", 24),
    padx=30,
    pady=10
)
no_btn.place(x=260, y=10)


def dodge(e):
    no_btn.place(x=260, y=10)  # stays put but feels fake-choice 😉


no_btn.bind("<Enter>", dodge)

root.mainloop()
