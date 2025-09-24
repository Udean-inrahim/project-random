#nama file tebak angka.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import random

def jawab(event=None):
    angka = entry.get().strip()
    if not angka:
        messagebox.showinfo("Kosong", "Masukin dulu angkanya")
        return

    kata = random.choice(["Scan kepala... 🧠", "Mikir keras 🥵"])
    result_label.config(text=kata, fg="red", bg="yellow")
    root.update()
    root.after(1500, lambda: reveal(angka))

def reveal(angka):
    # Bersihkan isi frame dulu biar ga numpuk
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Gambar kiri
    try:
        img1 = Image.open("gambar2.jpg")   # ganti dengan file gambar sebelah kiri
        img1 = img1.resize((100, 100))
        photo1 = ImageTk.PhotoImage(img1)
        img1_label = tk.Label(result_frame, image=photo1, bg="black")
        img1_label.image = photo1  # simpan reference
        img1_label.pack(side="left", padx=10)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal load gambar kiri: {e}")

    # Teks di tengah
    text_label = tk.Label(result_frame,
                          text=f"kamu mikirin angka {angka}",
                          fg="red", bg="white",
                          font=("Comic Sans MS", 16, "bold"))
    text_label.pack(side="left", padx=10)

    # Gambar kanan
    try:
        img2 = Image.open("gambar1.jpg")   # ganti dengan file gambar sebelah kanan
        img2 = img2.resize((100, 100))
        photo2 = ImageTk.PhotoImage(img2)
        img2_label = tk.Label(result_frame, image=photo2, bg="black")
        img2_label.image = photo2
        img2_label.pack(side="left", padx=10)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal load gambar kanan: {e}")



def reset():
    entry.delete(0, tk.END)
    result_label.config(text="", fg="black", bg="white")
    entry.focus_set()

root = tk.Tk()
root.title("Tebak Angka")
root.geometry("500x400")
root.configure(bg="black")  

# Tambah gambar meme
try:
    img = Image.open("meme.jpg")   # pastikan ada file meme.png di folder yg sama
    img = img.resize((120, 120))
    meme_img = ImageTk.PhotoImage(img)
    meme_label = tk.Label(root, image=meme_img, bg="black")
    meme_label.pack(pady=8)
except:
    meme_label = tk.Label(root, text="(Meme hilang 😭)", bg="red", fg="white")
    meme_label.pack(pady=8)

prompt = tk.Label(root,
                  text="TEBAK PIKIRAN, MASUKKAN ANGKA",
                  wraplength=400,
                  justify="center",
                  font=("Comic Sans MS", 12, "bold"),
                  fg="blue",
                  bg="white")
prompt.pack(pady=6)

entry = tk.Entry(root, font=("Comic Sans MS", 16, "bold"), justify="center", fg="cyan", bg="black")
entry.pack(pady=6, ipadx=10, ipady=4)
entry.focus_set()
entry.bind("<Return>", jawab)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=6)

jawab_btn = tk.Button(button_frame, text="🔥 Jawab 🔥", width=12,
                      command=jawab, bg="red", fg="white", font=("Comic Sans MS", 10, "bold"))
jawab_btn.pack(side="left", padx=6)

reset_btn = tk.Button(button_frame, text="🔄 Ulangi 🔄", width=12,
                      command=reset, bg="blue", fg="white", font=("Comic Sans MS", 10, "bold"))
reset_btn.pack(side="left", padx=6)

result_label = tk.Label(root, text="", font=("Comic Sans MS", 16, "bold"), bg="black")
result_label.pack(pady=(20, 6))

# Frame untuk hasil (teks + gambar kiri/kanan)
result_frame = tk.Frame(root, bg="black")
result_frame.pack(pady=(20, 6))

root.mainloop()
