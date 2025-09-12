import tkinter as tk
from tkinter import ttk, messagebox
from models.inventory import Inventory
from models.sales import Sales
import datetime

class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Administrador")
        self.root.geometry("700x400")

        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        title = tk.Label(frame, text="Panel Administrador", font=("Arial", 16, "bold"), bg="white")
        title.pack(pady=10)

        btn_frame = tk.Frame(frame, bg="white")
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="📦 Gestionar Inventario", command=self.gestionar_inventario, width=25).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="📊 Ver Utilidad", command=self.ver_utilidad, width=25).grid(row=0, column=1, padx=10, pady=10)

    def gestionar_inventario(self):
        win = tk.Toplevel(self.root)
        win.title("Gestión de Inventario")
        win.geometry("700x400")

        cols = ("ID", "Nombre", "Costo", "Precio", "Stock")
        self.tree = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        self.cargar_productos()

        btns = tk.Frame(win)
        btns.pack(pady=5)
        ttk.Button(btns, text="Agregar Producto", command=self.agregar_producto).pack(side="left", padx=10)
        ttk.Button(btns, text="Eliminar Producto", command=self.eliminar_producto).pack(side="left", padx=10)

    def cargar_productos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        inventario = Inventory.cargar_inventario()
        for p in inventario:
            self.tree.insert("", "end", values=(p["id"], p["nombre"], p["costo"], p["precio"], p["stock"]))

    def agregar_producto(self):
        win = tk.Toplevel(self.root)
        win.title("Nuevo Producto")

        form = tk.Frame(win)
        form.pack(padx=10, pady=10)

        labels = ["ID", "Nombre", "Costo", "Precio", "Stock"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(form)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label.lower()] = entry

        def guardar():
            producto = {k: v.get() for k, v in self.entries.items()}
            Inventory.agregar_producto(producto)
            messagebox.showinfo("Éxito", "Producto agregado")
            win.destroy()
            self.cargar_productos()

        ttk.Button(win, text="Guardar", command=guardar).pack(pady=10)

    def eliminar_producto(self):
        item = self.tree.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un producto")
            return
        producto_id = self.tree.item(item, "values")[0]
        Inventory.eliminar_producto(producto_id)
        self.cargar_productos()

    def ver_utilidad(self):
        win = tk.Toplevel(self.root)
        win.title("Consulta de Utilidad")

        tk.Label(win, text="Fecha inicio (YYYY-MM-DD)").pack()
        entry_inicio = ttk.Entry(win)
        entry_inicio.pack()

        tk.Label(win, text="Fecha fin (YYYY-MM-DD)").pack()
        entry_fin = ttk.Entry(win)
        entry_fin.pack()

        def calcular():
            try:
                inicio = datetime.date.fromisoformat(entry_inicio.get())
                fin = datetime.date.fromisoformat(entry_fin.get())
                utilidad = Sales.calcular_utilidad(inicio, fin)
                messagebox.showinfo("Resultado", f"Utilidad: {utilidad}")
            except Exception:
                messagebox.showerror("Error", "Formato de fecha incorrecto")

        ttk.Button(win, text="Calcular", command=calcular).pack(pady=10)
