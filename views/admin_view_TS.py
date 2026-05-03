import tkinter as tk
from tkinter import ttk, messagebox
from models.inventory import Inventory
from models.sales import Sales
from models.providers import Providers  # 👈 Importar proveedores
from tkcalendar import Calendar
import datetime


def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


class AdminView_TecnoStyle:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel Administrador")

        centrar_ventana(self.root, 1000, 720)
        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        title = tk.Label(frame, text="Panel Administrador", font=("Arial", 16, "bold"), bg="white")
        title.pack(pady=10)

        btn_frame = tk.Frame(frame, bg="white")
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="📦 Gestionar Inventario", command=self.gestionar_inventario, width=25).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(btn_frame, text="📊 Ver Utilidad", command=self.ver_utilidad, width=25).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(btn_frame, text="👤 Gestionar Proveedores", command=self.gestionar_proveedores, width=25).grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(btn_frame, text="🧾 Reporte de Ventas", command=self.ver_ventas, width=25).grid(row=0, column=3, padx=10, pady=10)
        ttk.Button(btn_frame, text="🏆 Productos más vendidos", command=self.ver_top_productos, width=25).grid(row=1, column=0, padx=10, pady=10)

    # ----------------------------
    # Inventario
    # ----------------------------
    def gestionar_inventario(self):
        win = tk.Toplevel(self.root)
        win.title("Gestión de Inventario")
        centrar_ventana(win, 1000, 720)
        win.configure(bg="#f0f0f0")
        search_frame = tk.Frame(win, bg="white")
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Buscar:", bg="white").pack(side="left", padx=5)
        search_entry = ttk.Entry(search_frame)
        search_entry.pack(side="left", padx=5)

        def buscar():
            query = search_entry.get().lower()
            for row in self.tree.get_children():
                self.tree.delete(row)
            inventario = Inventory.cargar_inventario()
            for p in inventario:
                if query in p["nombre"].lower() or query in p["id"].lower():
                    self.tree.insert("", "end", values=(p.get("id"), p.get("nombre"), p.get("costo"),
                                                        p.get("precio"), p.get("stock"), p.get("proveedor", "")))

        ttk.Button(search_frame, text="Buscar", command=buscar).pack(side="left", padx=5)


        cols = ("ID", "Nombre", "Costo", "Precio", "Stock", "Proveedor")
        self.tree = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        self.cargar_productos()

        btns = tk.Frame(win, bg="white")
        btns.pack(pady=5)
        ttk.Button(btns, text="Agregar Producto", command=self.agregar_producto).pack(side="left", padx=10)
        ttk.Button(btns, text="Eliminar Producto", command=self.eliminar_producto).pack(side="left", padx=10)

    def cargar_productos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        inventario = Inventory.cargar_inventario()
        for p in inventario:
            self.tree.insert("", "end", values=(p.get("id"), p.get("nombre"), p.get("costo"), p.get("precio"), p.get("stock"), p.get("proveedor", "")))

    def agregar_producto(self):
        win = tk.Toplevel(self.root)
        win.title("Nuevo Producto")
        centrar_ventana(win, 400, 400)

        form = tk.Frame(win)
        form.pack(padx=10, pady=10)

        labels = ["ID", "Nombre", "Costo", "Precio", "Stock"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(form)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[label.lower()] = entry

        # Combobox de proveedor
        tk.Label(form, text="Proveedor").grid(row=len(labels), column=0, padx=5, pady=5)
        proveedores = Providers.cargar_proveedores()
        lista_proveedores = [p["nombre"] for p in proveedores] if proveedores else []
        self.combo_proveedor = ttk.Combobox(form, values=lista_proveedores, state="readonly")
        self.combo_proveedor.grid(row=len(labels), column=1, padx=5, pady=5)

        def guardar():
            producto = {k: v.get() for k, v in self.entries.items()}
            producto["proveedor"] = self.combo_proveedor.get()
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

    # ----------------------------
    # Proveedores
    # ----------------------------
    def gestionar_proveedores(self):
        win = tk.Toplevel(self.root)
        win.title("Gestión de Proveedores")
        centrar_ventana(win, 600, 400)

        cols = ("ID", "Nombre", "Telefono", "Email")
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        def cargar():
            for row in tree.get_children():
                tree.delete(row)
            for p in Providers.cargar_proveedores():
                tree.insert("", "end", values=(p["id"], p["nombre"], p["telefono"], p["email"]))

        def agregar():
            sub = tk.Toplevel(win)
            sub.title("Nuevo Proveedor")
            centrar_ventana(sub, 400, 300)

            labels = ["ID", "Nombre", "Telefono", "Email"]
            entradas = {}
            for i, label in enumerate(labels):
                tk.Label(sub, text=label).grid(row=i, column=0, padx=5, pady=5)
                entry = ttk.Entry(sub)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entradas[label.lower()] = entry

            def guardar():
                proveedor = {k: v.get() for k, v in entradas.items()}
                Providers.agregar_proveedor(proveedor)
                sub.destroy()
                cargar()

            ttk.Button(sub, text="Guardar", command=guardar).grid(row=len(labels), column=0, columnspan=2, pady=10)

        def eliminar():
            item = tree.selection()
            if not item:
                messagebox.showerror("Error", "Seleccione un proveedor")
                return
            proveedor_id = tree.item(item, "values")[0]
            Providers.eliminar_proveedor(proveedor_id)
            cargar()

        btns = tk.Frame(win, bg="white")
        btns.pack(pady=5)
        ttk.Button(btns, text="Agregar Proveedor", command=agregar).pack(side="left", padx=10)
        ttk.Button(btns, text="Eliminar Proveedor", command=eliminar).pack(side="left", padx=10)

        cargar()

    # ----------------------------
    # Reporte de Utilidad
    # ----------------------------
    def ver_utilidad(self):
        win = tk.Toplevel(self.root)
        win.title("Consulta de Utilidad")

        centrar_ventana(win, 600, 400)
        win.configure(bg="white")

        frame = tk.Frame(win, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="Fecha inicio:", bg="white", font=("Arial", 11)).pack(pady=5)
        cal_inicio = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
        cal_inicio.pack(pady=5)

        tk.Label(frame, text="Fecha fin:", bg="white", font=("Arial", 11)).pack(pady=5)
        cal_fin = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
        cal_fin.pack(pady=5)

        def calcular():
            try:
                inicio = datetime.date.fromisoformat(cal_inicio.get_date())
                fin = datetime.date.fromisoformat(cal_fin.get_date())
                utilidad = Sales.calcular_utilidad(inicio, fin)
                messagebox.showinfo("Resultado", f"Utilidad entre {inicio} y {fin}: {utilidad}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema: {e}")

        ttk.Button(frame, text="Calcular Utilidad", command=calcular).pack(pady=15)


    # ----------------------------
    # Reporte de Ventas
    # ----------------------------
    def ver_ventas(self):
        win = tk.Toplevel(self.root)
        win.title("Consulta de Ventas")

        centrar_ventana(win, 600, 400)
        win.configure(bg="white")

        frame = tk.Frame(win, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="Fecha inicio:", bg="white", font=("Arial", 11)).pack(pady=5)
        cal_inicio = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
        cal_inicio.pack(pady=5)

        tk.Label(frame, text="Fecha fin:", bg="white", font=("Arial", 11)).pack(pady=5)
        cal_fin = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
        cal_fin.pack(pady=5)

        def calcular_ventas():
            try:
                inicio = datetime.date.fromisoformat(cal_inicio.get_date())
                fin = datetime.date.fromisoformat(cal_fin.get_date())
                ventas = Sales.calcular_ventas(inicio, fin)
                messagebox.showinfo("Resultado", f"Ventas entre {inicio} y {fin}: {ventas}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un problema: {e}")

        ttk.Button(frame, text="Calcular Ventas", command=calcular_ventas).pack(pady=15)

    # ----------------------------
    # Cierres de caja
    # ----------------------------


    # ----------------------------
    # Ranking de productos más vendidos
    # ----------------------------

    def ver_top_productos(self):
        win = tk.Toplevel(self.root)
        win.title("Productos más vendidos")
        centrar_ventana(win, 600, 400)
        win.configure(bg="white")

        frame = tk.Frame(win, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        cols = ("Producto", "Cantidad Vendida")
        tree = ttk.Treeview(frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        def cargar_ranking(dias):
            for row in tree.get_children():
                tree.delete(row)
            hoy = datetime.date.today()
            inicio = hoy - datetime.timedelta(days=dias)
            ranking = Sales.productos_mas_vendidos(inicio, hoy)
            for nombre, cantidad in ranking:
                tree.insert("", "end", values=(nombre, cantidad))

        btns = tk.Frame(win, bg="white")
        btns.pack(pady=10)

        ttk.Button(btns, text="Hoy", command=lambda: cargar_ranking(0)).pack(side="left", padx=5)
        ttk.Button(btns, text="Últimos 7 días", command=lambda: cargar_ranking(7)).pack(side="left", padx=5)
        ttk.Button(btns, text="Últimos 30 días", command=lambda: cargar_ranking(30)).pack(side="left", padx=5)

        cargar_ranking(0)  # Mostrar por defecto los de hoy
 