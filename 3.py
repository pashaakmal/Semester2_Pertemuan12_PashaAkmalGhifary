import tkinter as tk

window = tk.Tk()
window.title("Aplikasi Sederhana")


label = tk.Label(window, text="Selamat datang di aplikasi sederhana!")
label.pack(padx=10, pady=10)


def on_button_click():
    label.config(text="Tombol ditekan!")

button = tk.Button(window, text="Klik saya", command=on_button_click)
button.pack(padx=10, pady=10)


entry = tk.Entry(window)
entry.pack(padx=10, pady=10)


text_area = tk.Text(window, height=5, width=30)
text_area.pack(padx=10, pady=10)


frame = tk.Frame(window)
frame.pack(padx=10, pady=10)


canvas = tk.Canvas(frame, bg="white", height=100, width=200)
canvas.pack()


window.mainloop()
