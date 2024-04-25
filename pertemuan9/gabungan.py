import tkinter as tk
from tkinter import messagebox


def tes_tombol():
    nama = Entryku.get()
    messagebox.showinfo("Info", f"Berhasil Menginput Nama Anda {nama}. Terima Kasih!")


def animate_text():
    current_text = text.get("1.0", "end-1c")
    text.delete("1.0", tk.END)
    text.insert(tk.END, current_text[1:] + current_text[0])
    text.after(100, animate_text)


def animate_blink_text():
    # Ambil posisi awal teks
    start_index = "1.0"
    end_index = "1.4"

    # Jika posisi teks berada di kanan (akhir teks)
    if text.tag_nextrange("blink", "1.0") is None:
        # Geser teks ke awal (kiri)
        text.delete(start_index, end_index)
        text.insert(tk.END, " ")
    else:
        # Geser teks ke kanan
        char = text.get(start_index)
        text.delete(start_index)
        text.insert(tk.END, char)

    text.after(500, animate_blink_text)


# Inisialisasi root window
root = tk.Tk()
root.geometry("600x600")
root.title("Aplikasi GUI Gabungan")

# Membuat frame utama
Frameku = tk.Frame(root, bg='lightblue', padx=20, pady=20)
Frameku.pack(fill=tk.BOTH, expand=True)

# Label dan Entry
label_nama = tk.Label(Frameku, text="Nama Anda:", bg='lightblue', font=("Arial", 12))
label_nama.pack(pady=5)
Entryku = tk.Entry(Frameku, bg='lightgreen', bd=2, relief=tk.SOLID, font=("Arial", 12))
Entryku.pack(pady=5, fill=tk.X)

# Tombol
Tombolku = tk.Button(Frameku, text="Submit", bg='gray', fg='white', command=tes_tombol, font=("Arial", 12))
Tombolku.pack(pady=10)

# Canvas
C = tk.Canvas(Frameku, bg="white", height=250, width=500, bd=2, relief=tk.SOLID)
coord = 50, 50, 450, 200
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(50, 50, 250, 250, fill='blue')
C.pack(pady=10)

# Label Frame
label_frame = tk.LabelFrame(Frameku, text="Pilihan Anda", bg='lightblue', padx=10, pady=10)
label_frame.pack(pady=10, fill=tk.X)

var = tk.StringVar()
label = tk.Label(label_frame, textvariable=var, bg='lightblue', fg='black', font=("Arial", 12))
var.set("Pilih kesukaan Anda")
label.pack()

# Checkboxes
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
CheckVar3 = tk.IntVar()

C1 = tk.Checkbutton(label_frame, text="Mendengarkan Music", variable=CheckVar1, onvalue=1, offvalue=0, bg='lightblue',
                    font=("Arial", 12))
C2 = tk.Checkbutton(label_frame, text="Menonton Video", variable=CheckVar2, onvalue=1, offvalue=0, bg='lightblue',
                    font=("Arial", 12))
C3 = tk.Checkbutton(label_frame, text="Traveling", variable=CheckVar3, onvalue=1, offvalue=0, bg='lightblue',
                    font=("Arial", 12))

C1.pack(pady=5, anchor=tk.W)
C2.pack(pady=5, anchor=tk.W)
C3.pack(pady=5, anchor=tk.W)

# Text Widget
text = tk.Text(Frameku, height=5, bg='lightyellow', font=("Courier New", 14, "bold italic"))
text.insert(tk.INSERT, "Terima Kasih ")
text.insert(tk.END, "Bye Bye.....")
text.pack(pady=10)

# Gradient background for Text Widget
for i in range(1, 6):
    text.tag_configure(f"bg_gradient_{i}", background=f"#{i * 2:02x}{i * 2:02x}ff")
    text.tag_add(f"bg_gradient_{i}", "1.0", "end-1c")

# Blink text
text.tag_add("blink", "1.0", "1.4")
text.tag_configure("blink", foreground="red")
text.after(500, lambda: text.tag_remove("blink", "1.0", "end"))
text.after(1000, lambda: text.tag_add("blink", "1.0", "1.4"))
text.after(1500, lambda: text.tag_remove("blink", "1.0", "end"))

# Center blink text
text.tag_configure("center", justify='center')
text.tag_add("center", "1.0", "end")

# Animate text
animate_text()

# Animate blink text
animate_blink_text()

root.mainloop()
