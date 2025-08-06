import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
from PIL import Image, ImageTk
import os


VENTAS_FILE = "data/ventas.csv"

def launch_employee_interface():
    root = tk.Tk()
    app = EmployeeView(root)
    root.mainloop()

class EmployeeView:
    def __init__(self, master):
        self.master = master
        self.master.title("Panel Empleado - TecnoImpacto")
        self.master.geometry("700x550")
        self.master.configure(bg="#f9f9f9")
        self.encabezado = tk.Frame(self.master, bg="#ffffff")
        self.encabezado.pack(fill="x")
        self.agregar_logo_encabezado()
        self.build_ui()
        self.load_ventas_dia()

    def agregar_logo_encabezado(self):
        logo_path = os.path.join("assets", "TecnoImpacto.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path)
            img = img.resize((400, 120))
            self.logo_img = ImageTk.PhotoImage(img)
            logo_label = tk.Label(self.encabezado, image=self.logo_img, bg="#ffffff")
            logo_label.pack(pady=10)
        else:
            label = tk.Label(self.encabezado, text="TecnoImpacto", font=("Arial", 20, "bold"), bg="#ffffff")
            label.pack(pady=10)

    def build_ui(self):
        # Sección registro
        frame_registro = ttk.LabelFrame(self.master, text="Registrar Venta")
        frame_registro.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_registro, text="Cantidad:").grid(row=0, column=0, padx=5, pady=5)
        self.cantidad_var = tk.IntVar(value=1)
        self.cantidad_entry = ttk.Entry(frame_registro, textvariable=self.cantidad_var, width=10)
        self.cantidad_entry.grid(row=0, column=1)

        ttk.Label(frame_registro, text="Producto:").grid(row=0, column=2, padx=5, pady=5)
        self.producto_var = tk.StringVar()

        from widgets.autocomplete import AutocompleteEntry
        from views.datos_productos import SUGERENCIAS_PRODUCTO
        self.producto_entry = AutocompleteEntry(
            palabras_clave=SUGERENCIAS_PRODUCTO,
            master=frame_registro,
            textvariable=self.producto_var,
            width=30
        )
        self.producto_entry.grid(row=0, column=3)

        ttk.Label(frame_registro, text="Precio Unitario:").grid(row=0, column=4, padx=5, pady=5)
        self.precio_var = tk.DoubleVar()
        self.precio_entry = ttk.Entry(frame_registro, textvariable=self.precio_var, width=10)
        self.precio_entry.grid(row=0, column=5)

        self.total_label = ttk.Label(frame_registro, text="Total: $0.00", font=("Arial", 10, "bold"))
        self.total_label.grid(row=0, column=6, padx=10)

        self.precio_var.trace("w", self.update_total)
        self.cantidad_var.trace("w", self.update_total)

        ttk.Button(frame_registro, text="Registrar", command=self.registrar_venta).grid(row=0, column=7, padx=10)

        # Tabla de ventas del día
        self.tree = ttk.Treeview(self.master, columns=("fecha", "cantidad", "producto", "unitario", "total"), show="headings")
        for col in ("fecha", "cantidad", "producto", "unitario", "total"):
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Total diario
        self.total_dia_label = ttk.Label(self.master, text="Total del día: $0.00", font=("Arial", 12))
        self.total_dia_label.pack(pady=5)

    def update_total(self, *args):
        try:
            cantidad = self.cantidad_var.get()
            precio = self.precio_var.get()
            total = cantidad * precio
            self.total_label.config(text=f"Total: ${total:.2f}")
        except:
            self.total_label.config(text="Total: $0.00")

    def registrar_venta(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        cantidad = self.cantidad_var.get()
        producto = self.producto_var.get()
        unitario = self.precio_var.get()
        total = cantidad * unitario

        if not producto or unitario <= 0:
            messagebox.showerror("Error", "Complete todos los campos correctamente.")
            return

        with open(VENTAS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([fecha, cantidad, producto, unitario, total])

        self.tree.insert("", "end", values=(fecha, cantidad, producto, unitario, total))
        self.reset_fields()
        self.actualizar_total_dia()

    def load_ventas_dia(self):
        hoy = datetime.now().strftime("%Y-%m-%d")
        total_dia = 0

        if os.path.exists(VENTAS_FILE):
            with open(VENTAS_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == hoy:
                        self.tree.insert("", "end", values=row)
                        total_dia += float(row[4])

        self.total_dia_label.config(text=f"Total del día: ${total_dia:2}")

    def reset_fields(self):
        self.cantidad_var.set(1)
        self.producto_var.set("")
        self.precio_var.set(0.0)

    def actualizar_total_dia(self):
        total = 0.0
        for item in self.tree.get_children():
            total += float(self.tree.item(item)['values'][4])
        self.total_dia_label.config(text=f"Total del día: ${total:2}")
