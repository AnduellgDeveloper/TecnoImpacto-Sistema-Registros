import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
from models.sales import guardar_venta, ventas_por_periodo, ventas_del_dia, leer_ventas, productos_mas_vendidos
from PIL import Image, ImageTk

VENTAS_FILE = "data/ventas.csv"

def launch_admin_interface():
    root = tk.Tk()
    app = AdminView(root)
    root.mainloop()

class AdminView:
    def __init__(self, master):
        self.master = master
        self.master.title("Panel Administrador - TecnoImpacto")
        self.master.geometry("800x600")
        self.master.configure(bg="#f2f2f2")

        self.encabezado = tk.Frame(self.master, bg="#ffffff")
        self.encabezado.pack(fill="x")
        self.agregar_logo_encabezado()

        self.ventas = []
        self.build_ui()
        self.load_ventas()

    def agregar_logo_encabezado(self):
        logo_path = os.path.join("assets", "TecnoImpacto.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((400, 120))
            self.logo_img = ImageTk.PhotoImage(img)
            logo_label = tk.Label(self.encabezado, image=self.logo_img, bg="#ffffff")
            logo_label.pack(pady=10)
        else:
            label = tk.Label(self.encabezado, text="TecnoImpacto", font=("Arial", 20, "bold"), bg="#ffffff")
            label.pack(pady=10)

    def build_ui(self):
        # Topbar fija arriba
        topbar = ttk.Frame(self.master)
        topbar.pack(fill="x", padx=10, pady=5)
        ttk.Button(topbar, text="📊 Ver productos más vendidos", command=self.mostrar_ventana_resumen).pack(side="right")

        # Contenedor principal
        contenedor = ttk.Frame(self.master)
        contenedor.pack(fill="both", expand=True)

        # Registro de ventas
        frame_registro = ttk.LabelFrame(contenedor, text="Registro de Venta")
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

        # Tabla de ventas con scrollbar
        frame_tabla = ttk.Frame(contenedor)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("fecha", "cantidad", "producto", "unitario", "total"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        for col in ("fecha", "cantidad", "producto", "unitario", "total"):
            self.tree.heading(col, text=col.capitalize())

        self.tree.pack(fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)

        self.tree.bind("<Double-1>", self.edit_item)

        # Totales
        self.total_frame = ttk.LabelFrame(contenedor, text="Totales")
        self.total_frame.pack(fill="x", padx=10, pady=10)

        self.total_dia = ttk.Label(self.total_frame, text="Ventas del día: $0.00")
        self.total_dia.pack(side="left", padx=10)

        self.total_semana = ttk.Label(self.total_frame, text="Semana: $0.00")
        self.total_semana.pack(side="left", padx=10)

        self.total_mes = ttk.Label(self.total_frame, text="Mes: $0.00")
        self.total_mes.pack(side="left", padx=10)

        self.total_anio = ttk.Label(self.total_frame, text="Año: $0.00")
        self.total_anio.pack(side="left", padx=10)

    def update_total(self, *args):
        try:
            cantidad = self.cantidad_var.get()
            precio = self.precio_var.get()
            total = cantidad * precio
            self.total_label.config(text=f"Total: ${total:2}")
        except:
            self.total_label.config(text="Total: $0.00")

    def registrar_venta(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        cantidad = self.cantidad_var.get()
        producto = self.producto_var.get()
        unitario = self.precio_var.get()
        total = cantidad * unitario

        if not producto or unitario <= 0:
            messagebox.showerror("Error", "Ingrese todos los datos correctamente.")
            return

        guardar_venta(fecha, cantidad, producto, unitario, total)

        self.tree.insert("", "end", values=(fecha, cantidad, producto, f"${unitario:2}", f"${total:2}"))
        self.reset_fields()
        self.actualizar_totales()

    def load_ventas(self):
        for venta in leer_ventas():
            self.tree.insert("", "end", values=(
                venta["fecha"].strftime("%Y-%m-%d"),
                venta["cantidad"],
                venta["producto"],
                f"${venta['unitario']:2}",
                f"${venta['total']:2}"
            ))
        self.actualizar_totales()

    def reset_fields(self):
        self.cantidad_var.set(1)
        self.producto_var.set("")
        self.precio_var.set(0.0)

    def actualizar_totales(self):
        self.total_dia.config(text=f"Ventas del día: ${ventas_por_periodo('dia'):2}")
        self.total_semana.config(text=f"Semana: ${ventas_por_periodo('semana'):2}")
        self.total_mes.config(text=f"Mes: ${ventas_por_periodo('mes'):2}")
        self.total_anio.config(text=f"Año: ${ventas_por_periodo('anio'):2}")

    def edit_item(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        valores = self.tree.item(selected)["values"]
        self.cantidad_var.set(valores[1])
        self.producto_var.set(valores[2])
        self.precio_var.set(float(str(valores[3]).replace("$", "")))
        self.tree.delete(selected)

    def mostrar_ventana_resumen(self):
        resumen_window = tk.Toplevel(self.master)
        resumen_window.title("Resumen de productos más vendidos")
        resumen_window.geometry("500x400")

        periodo_var = tk.StringVar(value="dia")

        def cargar_tabla():
            for row in tree.get_children():
                tree.delete(row)
            data = productos_mas_vendidos(periodo_var.get())
            for producto, cantidad, total in data:
                tree.insert("", "end", values=(producto, cantidad, f"${total:2}"))

        frame_select = ttk.Frame(resumen_window)
        frame_select.pack(pady=10)

        ttk.Label(frame_select, text="Ver por:").pack(side="left", padx=5)
        ttk.Combobox(frame_select, textvariable=periodo_var, values=["dia", "semana", "mes", "anio"], width=10).pack(side="left", padx=5)
        ttk.Button(frame_select, text="Actualizar", command=cargar_tabla).pack(side="left", padx=5)

        tree = ttk.Treeview(resumen_window, columns=("producto", "cantidad", "total"), show="headings")
        tree.heading("producto", text="Producto")
        tree.heading("cantidad", text="Cantidad")
        tree.heading("total", text="Total")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        cargar_tabla()
