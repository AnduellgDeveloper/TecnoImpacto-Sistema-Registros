import tkinter as tk
from tkinter import ttk, messagebox
from models.sales import Sales
from models.inventory import Inventory
import datetime
import unicodedata


class EmployeeView:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Vendedor")
        self.root.geometry("700x500")

        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        title = tk.Label(frame, text="Registrar Venta", font=("Arial", 16, "bold"), bg="white")
        title.pack(pady=10)

        # --- Autocompletado ---
        tk.Label(frame, text="Producto:", bg="white").pack()
        self.entry_producto = tk.Entry(frame)
        self.entry_producto.pack(pady=5)
        self.entry_producto.bind("<KeyRelease>", self.sugerir_productos)
        # --- Tabla sugerencias ---
        scroll_y = tk.Scrollbar(frame, orient="vertical")
        scroll_y.pack(side="right", fill="y")
        self.listbox_sugerencias = tk.Listbox(
            frame, height=10, width=50, yscrollcommand=scroll_y.set
        )
        self.listbox_sugerencias.pack(pady=5, fill="x")
        scroll_y.config(command=self.listbox_sugerencias.yview)
        self.listbox_sugerencias.bind("<<ListboxSelect>>", self.seleccionar_producto)

        # --- Info del producto ---
        self.lbl_info = tk.Label(frame, text="Costo: - | Precio: -", bg="white", font=("Arial", 11))
        self.lbl_info.pack(pady=5)

        # --- Cantidad ---
        tk.Label(frame, text="Cantidad:", bg="white").pack()
        self.entry_cantidad = ttk.Entry(frame)
        self.entry_cantidad.pack(pady=5)

        # --- Descuento ---
        tk.Label(frame, text="Descuento (en $):", bg="white").pack()
        self.entry_descuento = ttk.Entry(frame)
        self.entry_descuento.pack(pady=5)

        # --- Botón ---
        ttk.Button(frame, text="Registrar Venta", command=self.registrar_venta).pack(pady=10)

        # --- Tabla de ventas del día ---
        cols = ("Producto", "Cantidad", "Precio Final", "Descuento", "Total", "Utilidad")
        self.tree = ttk.Treeview(frame, columns=cols, show="headings", height=8)
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.producto_seleccionado = None

    # --- Función de normalización ---
    @staticmethod
    def normalizar_texto(texto):
        """Convierte texto a minúsculas y sin acentos."""
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto.lower())
            if unicodedata.category(c) != 'Mn'
        )

    # --- Autocompletado ---
    def sugerir_productos(self, event):
        texto = self.normalizar_texto(self.entry_producto.get())
        self.listbox_sugerencias.delete(0, tk.END)

        if texto:
            inventario = Inventory.cargar_inventario()
            resultados = []
            for p in inventario:
                nombre = self.normalizar_texto(p["nombre"])
                pid = self.normalizar_texto(p["id"])
                if texto in nombre or texto in pid:
                    resultados.append(f'{p["id"]} - {p["nombre"]}')

            # Ordenar resultados: primero los que empiezan con el texto
            resultados = sorted(resultados, key=lambda x: not self.normalizar_texto(x).startswith(texto))

            for r in resultados:
                self.listbox_sugerencias.insert(tk.END, r)

    # --- Seleccionar producto ---
    def seleccionar_producto(self, event):
        seleccion = self.listbox_sugerencias.get(tk.ACTIVE)
        if not seleccion:
            return
        producto_id = seleccion.split(" - ")[0]
        inventario = Inventory.cargar_inventario()
        self.producto_seleccionado = next((p for p in inventario if p["id"] == producto_id), None)
        if self.producto_seleccionado:
            self.lbl_info.config(text=f'Costo: {self.producto_seleccionado["costo"]} | '
                                      f'Precio: {self.producto_seleccionado["precio"]}')

    # --- Registrar venta ---
    def registrar_venta(self):
        if not self.producto_seleccionado:
            messagebox.showerror("Error", "Seleccione un producto válido")
            return

        try:
            cantidad = int(self.entry_cantidad.get())
            descuento = int(self.entry_descuento.get() or 0)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos en cantidad y descuento")
            return

        precio_unit = int(self.producto_seleccionado["precio"])
        costo = int(self.producto_seleccionado["costo"])
        precio_final = max(precio_unit - descuento, 0)
        total = precio_final * cantidad
        utilidad = (precio_final - costo) * cantidad

        # Registrar venta en CSV
        try:
            Sales.registrar_venta(self.producto_seleccionado["id"], cantidad)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        # Mostrar en tabla
        self.tree.insert("", "end", values=(
            self.producto_seleccionado["nombre"],
            cantidad,
            precio_final,
            descuento,
            total,
            utilidad
        ))

        messagebox.showinfo("Éxito", "Venta registrada")
