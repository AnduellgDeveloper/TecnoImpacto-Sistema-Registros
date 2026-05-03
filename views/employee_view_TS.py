import tkinter as tk
from tkinter import ttk, messagebox
from models.sales_TS import Sales
from models.inventory_TS import Inventory
import datetime
import unicodedata
from models.repairs_TS import Repairs


def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

class EmployeeView_TecnoStyle:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Vendedor")
        
        centrar_ventana(self.root,1000, 720)
        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        title = tk.Label(frame, text="Registrar Venta", font=("Arial", 16, "bold"), bg="white")
        title.pack(pady=10)
        # --- Frame para botones ---
        frame_botones = tk.Frame(frame, bg="white")
        # --- Botón Registrar Arreglo ---
        ttk.Button(
            frame_botones,
            text="Registrar Arreglo",
            command=self.abrir_modal_arreglo
        ).pack(side="left", padx=10)



        # --- Autocompletado ---
        tk.Label(frame, text="Producto:", bg="white").pack()
        self.entry_producto = tk.Entry(frame)
        self.entry_producto.pack(pady=5)
        self.entry_producto.bind("<KeyRelease>", self.sugerir_productos)

        self.listbox_sugerencias = tk.Listbox(frame, height=8, width=60)
        self.listbox_sugerencias.pack(pady=5, fill="x")
        self.listbox_sugerencias.bind("<<ListboxSelect>>", self.seleccionar_producto)

        # --- Info del producto (Visual)---
        self.lbl_info = tk.Label(frame, text="Nombre: - | Stock: - | Precio: -", bg="white", font=("Arial", 11))
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
        cols = ("Producto", "Cantidad", "Precio Final", "Descuento", "Total")
        self.tree = ttk.Treeview(frame, columns=cols, show="headings", height=10)
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.producto_seleccionado = None

        # 🚀 Cargar ventas del día al iniciar
        self.cargar_ventas_del_dia()

        # ================= BUSCADOR REUTILIZABLE =================
    def buscar_productos(self, texto):
        texto = self.normalizar_texto(texto)
        if not texto:
            return []

        palabras = texto.split()
        inventario = Inventory.cargar_inventario()
        resultados = []

        for p in inventario:
            nombre = self.normalizar_texto(p["nombre"])
            pid = self.normalizar_texto(p["id"])
            texto_completo = f"{pid} {nombre}"

            if all(palabra in texto_completo for palabra in palabras):
                resultados.append(p)

        return resultados


    # --- Función de normalización ---
    @staticmethod
    def normalizar_texto(texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto.lower())
            if unicodedata.category(c) != 'Mn'
        )

    # --- Autocompletar ---
    def sugerir_productos(self, event):
        texto = self.normalizar_texto(self.entry_producto.get())
        self.listbox_sugerencias.delete(0, tk.END)

        if not texto:
            return

        palabras_busqueda = texto.split()  # 🔑 dividir por palabras
        inventario = Inventory.cargar_inventario()
        resultados = []

        for p in inventario:
            nombre = self.normalizar_texto(p["nombre"])
            pid = self.normalizar_texto(p["id"])

            texto_completo = f"{pid} {nombre}"

            # ✅ todas las palabras deben existir
            if all(palabra in texto_completo for palabra in palabras_busqueda):
                resultados.append(f'{p["id"]} - {p["nombre"]}')

        # Prioriza los que empiezan con la primera palabra
        resultados.sort(
            key=lambda x: not self.normalizar_texto(x).startswith(palabras_busqueda[0])
        )

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
            self.lbl_info.config(text=f'Nombre: {self.producto_seleccionado["nombre"]} | '
                                      f'Stock: {self.producto_seleccionado["stock"]} | '
                                      f'Precio: {self.producto_seleccionado["precio"]} | '
                                      )

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

        # Guardar en CSV con descuento y precio final
        try:
            Sales.registrar_venta(self.producto_seleccionado["id"], cantidad, descuento)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        # Refrescar ventas del día
        self.cargar_ventas_del_dia()
        messagebox.showinfo("Éxito", "Venta registrada")

    def abrir_modal_arreglo(self):
        win = tk.Toplevel(self.root)
        win.title("Registrar Arreglo")
        centrar_ventana(win, 400, 450)
        win.grab_set()

        campos = {}
        
        def campo(texto):
            tk.Label(win, text=texto).pack()
            e = ttk.Entry(win)
            e.pack(pady=3, fill="x", padx=20)
            return e
        
        campos["cliente"] = campo("Nombre del cliente")
        campos["telefono"] = campo("Teléfono")
        
        tk.Label(win, text="Descripción del arreglo").pack()
        txt_desc = tk.Text(win, height=4)
        txt_desc.pack(padx=20, pady=5, fill="x")

        campos["costo"] = campo("Costo del arreglo")
        campos["precio"] = campo("Precio al cliente")


        def guardar():
            try:
                cliente = campos["cliente"].get()
                telefono = campos["telefono"].get()
                descripcion = txt_desc.get("1.0", "end").strip()
                costo = int(campos["costo"].get())
                precio = int(campos["precio"].get())

                if not cliente or not descripcion:
                    raise ValueError("Campos obligatorios vacíos")

                venta = Repairs.registrar_arreglo(
                    cliente, telefono, descripcion, costo, precio
                )

                # 🔥 Guardar también como venta del día
                Sales.guardar_venta_directa(venta)

                self.cargar_ventas_del_dia()
                messagebox.showinfo("Éxito", "Arreglo registrado")
                win.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(win, text="Guardar Arreglo", command=guardar).pack(pady=15)





    # --- Cargar ventas del día ---
    def cargar_ventas_del_dia(self):
        self.tree.delete(*self.tree.get_children())
        ventas = Sales.cargar_ventas()
        hoy = datetime.date.today()

        for v in ventas:
            fecha = datetime.datetime.strptime(v["fecha"].strip(), "%Y-%m-%d").date()
            if fecha == hoy:
                self.tree.insert("", "end", values=(
                    v["nombre"],
                    v["cantidad"],
                    v["precio_final"],
                    v["descuento"],
                    v["total"],
                    #v["utilidad"]
                ))
    