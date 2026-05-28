import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from models.sales import Sales

from models.CashClosing import CashClosing

def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


class CashClosingView:

    def __init__(self, root):

        self.win = tk.Toplevel(root)
        self.win.title("Cierre de Caja")
        self.gastos = []
        centrar_ventana(self.win, 500, 720)
        self.win.configure(bg="#f0f0f0")
    

        self.crear_interfaz()
    
    # ---------------------------- Crear Interfaz ----------------------------
    def crear_interfaz(self):
        frame = tk.Frame(self.win)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        # ----------------------------
        # TITULO
        # ----------------------------
        titulo = tk.Label(frame,text="Cierre de Caja",font=("Arial", 16, "bold"))
        titulo.grid(row=1, column=0, columnspan=2, pady=10)
        # ----------------------------
        # FECHAS
        # ----------------------------
        hoy = datetime.date.today()
        inicio_mes = hoy.replace(day=1)
        # ----------------------------
        # CALCULOS
        # ----------------------------
        ventas_hoy = Sales.calcular_ventas(
            hoy,
            hoy
        )

        utilidad_hoy = Sales.calcular_utilidad(
            hoy,
            hoy
        )

        ventas_mes = Sales.calcular_ventas(
            inicio_mes,
            hoy
        )
        utilidad_mes = Sales.calcular_utilidad(
            inicio_mes,
            hoy
        )

        # =========================================================
        # FILA 1 -> VENTAS
        # =========================================================

        tk.Label(frame,text="Ventas del día:").grid(row=1,column=0,sticky="w",pady=5)
        self.lbl_ventas = tk.Label(
            frame,
            text=f"${ventas_hoy:,}",
            font=("Arial", 10, "bold")
        )
        self.lbl_ventas.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(0, 40)
        )

        tk.Label( frame,text="Ventas del mes:").grid(row=1,column=2,sticky="w")
        self.lbl_ventas_mes = tk.Label(
            frame,
            text=f"${ventas_mes:,}",
            font=("Arial", 10, "bold")
        )
        self.lbl_ventas_mes.grid(
            row=1,
            column=3,
            sticky="w"
        )

        # =========================================================
        # FILA 2 -> UTILIDADES
        # =========================================================

        tk.Label(
            frame,
            text="Utilidad del día:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.lbl_utilidad = tk.Label(
            frame,
            text=f"${utilidad_hoy:,}",
            font=("Arial", 10, "bold"),
            fg="green"
        )

        self.lbl_utilidad.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(0, 40)
        )

        tk.Label(
            frame,
            text="Utilidad del mes:"
        ).grid(
            row=2,
            column=2,
            sticky="w"
        )

        self.lbl_utilidad_mes = tk.Label(
            frame,
            text=f"${utilidad_mes:,}",
            font=("Arial", 10, "bold"),
            fg="green"
        )

        self.lbl_utilidad_mes.grid(
            row=2,
            column=3,
            sticky="w"
        )
        # ----------------------------
        # ARQUEO
        # ----------------------------

        separador = ttk.Separator(frame, orient="horizontal")
        separador.grid(row=6, column=0, columnspan=2, sticky="ew", pady=15)

        tk.Label(
            frame,
            text="Conteo de Caja",
            font=("Arial", 12, "bold")
        ).grid(row=4, column=0, columnspan=2, pady=10)

        # Gruesa

        tk.Label(
            frame,
            text="Gruesa:"
        ).grid(row=5, column=0, sticky="w", pady=5)

        self.entry_gruesa = ttk.Entry(frame)

        self.entry_gruesa.grid(row=5, column=1, sticky="ew")

        # Base

        tk.Label(frame,text="Base:").grid(row=6, column=0, sticky="w", pady=5)
        self.entry_base = ttk.Entry(frame)
        self.entry_base.grid(row=6, column=1, sticky="ew")

        # Sencilla

        tk.Label(frame,text="Sencilla:").grid(row=7, column=0, sticky="w", pady=5)
        self.entry_sencilla = ttk.Entry(frame)
        self.entry_sencilla.grid(row=7, column=1, sticky="ew")

        # Monedas 

        tk.Label(frame,text="Monedas:").grid(row=8, column=0, sticky="w", pady=5)
        self.entry_monedas = ttk.Entry(frame)
        self.entry_monedas.grid(row=8, column=1, sticky="ew")

        # ----------------------------
        # GASTOS
        # ----------------------------

        separador2 = ttk.Separator(
            frame,
            orient="horizontal"
        )

        separador2.grid(
            row=9,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=15
        )

        tk.Label(
            frame,
            text="Gastos del Día",
            font=("Arial", 12, "bold")
        ).grid(
            row=10,
            column=0,
            columnspan=2,
            pady=10
        )

        # TABLA GASTOS

        columnas = (
            "Tipo",
            "Descripción",
            "Valor",
            "Caja"
        )

        self.tree_gastos = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=5
        )

        for col in columnas:

            self.tree_gastos.heading(
                col,
                text=col
            )

        self.tree_gastos.grid(
            row=11,
            column=0,
            columnspan=2,
            pady=10
        )
        # ----------------------------
        # BOTON AGREGAR GASTO
        # ----------------------------
        ttk.Button(
            frame,
            text="Agregar Gasto",
            command=self.agregar_gasto
        ).grid(
            row=12,
            column=0,
            columnspan=2,
            pady=10
        )
        # ----------------------------
        # BOTON GENERAR
        # ----------------------------

        ttk.Button(
            frame,
            text="Generar Cierre",
            command=self.generar_cierre
        ).grid(
            row=9,
            column=0,
            columnspan=2,
            pady=20
        )

    # ---------------------------- Generar cierre ----------------------------
    def generar_cierre(self):

        try:

            # ----------------------------
            # CAPTURAR ARQUEO
            # ----------------------------

            arqueo = {

                    "gruesa": self.limpiar_numero(
                        self.entry_gruesa.get()
                    ),

                    "base": self.limpiar_numero(
                        self.entry_base.get()
                    ),

                    "sencilla": self.limpiar_numero(
                        self.entry_sencilla.get()
                    ),

                    "monedas": self.limpiar_numero(
                        self.entry_monedas.get()
                    )
                }

            # ----------------------------
            # DATOS TEMPORALES
            # ----------------------------

            # Luego esto lo conectarás con Sales

            ventas_sistema = 1000000
            ventas_efectivo = 800000
            utilidad_bruta = 250000

            gastos = self.gastos

            # ----------------------------
            # GENERAR CIERRE
            # ----------------------------

            resultado = CashClosing.generar_cierre(
                ventas_sistema,
                ventas_efectivo,
                utilidad_bruta,
                gastos,
                arqueo
            )

            # ----------------------------
            # MOSTRAR RESULTADO
            # ----------------------------

            messagebox.showinfo(
                "Cierre generado",
                f"""
        Caja real: ${resultado['caja_real']}

        Caja esperada: ${resultado['caja_esperada']}

        Diferencia: ${resultado['diferencia']}

        Utilidad neta: ${resultado['utilidad_neta']}
                """
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def agregar_gasto(self):

        win = tk.Toplevel(self.win)

        win.title("Agregar Gasto")

        frame = tk.Frame(win)
        frame.pack(padx=20, pady=20)

        # ----------------------------
        # TIPO
        # ----------------------------

        tk.Label(
            frame,
            text="Tipo"
        ).grid(row=0, column=0)

        combo_tipo = ttk.Combobox(

            frame,

            values=[
                "Nomina",
                "Flete",
                "Compra",
                "Servicios",
                "Arriendo",
                "Otros"
            ],

            state="readonly"
        )

        combo_tipo.grid(row=0, column=1)

        # ----------------------------
        # DESCRIPCION
        # ----------------------------

        tk.Label(
            frame,
            text="Descripción"
        ).grid(row=1, column=0)

        entry_descripcion = ttk.Entry(frame)
        entry_descripcion.grid(row=1, column=1)

        # ----------------------------
        # VALOR
        # ----------------------------
        tk.Label(
            frame,
            text="Valor"
        ).grid(row=2, column=0)

        entry_valor = ttk.Entry(frame)

        entry_valor.grid(row=2, column=1)

        # ----------------------------
        # AFECTA CAJA
        # ----------------------------

        afecta_caja = tk.BooleanVar(value=True)

        check = ttk.Checkbutton(
            frame,
            text="Afecta caja",
            variable=afecta_caja
        )

        check.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        # ----------------------------
        # GUARDAR
        # ----------------------------

        def guardar():

            try:

                gasto = {

                    "tipo": combo_tipo.get(),

                    "descripcion": entry_descripcion.get(),

                    "valor": self.limpiar_numero(
                        entry_valor.get()
                    ),

                    "afecta_caja": afecta_caja.get()
                }

                # GUARDAR EN LISTA

                self.gastos.append(gasto)

                # MOSTRAR EN TABLA

                self.tree_gastos.insert(

                    "",

                    "end",

                    values=(

                        gasto["tipo"],

                        gasto["descripcion"],

                        gasto["valor"],

                        "Sí" if gasto["afecta_caja"] else "No"
                    )
                )

                win.destroy()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        ttk.Button(
            frame,
            text="Guardar",
            command=guardar
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

    def limpiar_numero(self, valor):

            valor = valor.replace(".", "")
            valor = valor.replace(",", "")
            valor = valor.strip()

            return int(valor or 0)            