import tkinter as tk
from tkinter import ttk, messagebox

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
        centrar_ventana(self.win, 500, 720)
        self.win.configure(bg="#f0f0f0")
    

        self.crear_interfaz()

    def crear_interfaz(self):

        frame = tk.Frame(self.win)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # ----------------------------
        # TITULO
        # ----------------------------

        titulo = tk.Label(
            frame,
            text="Cierre de Caja",
            font=("Arial", 16, "bold")
        )

        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # ----------------------------
        # VENTAS DEL SISTEMA
        # ----------------------------

        tk.Label(
            frame,
            text="Ventas del sistema:"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.lbl_ventas = tk.Label(
            frame,
            text="$0"
        )

        self.lbl_ventas.grid(row=1, column=1, sticky="w")

        # ----------------------------
        # UTILIDAD BRUTA
        # ----------------------------

        tk.Label(
            frame,
            text="Utilidad bruta:"
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.lbl_utilidad = tk.Label(
            frame,
            text="$0"
        )

        self.lbl_utilidad.grid(row=2, column=1, sticky="w")

        # ----------------------------
        # ARQUEO
        # ----------------------------

        separador = ttk.Separator(frame, orient="horizontal")
        separador.grid(row=3, column=0, columnspan=2, sticky="ew", pady=15)

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

        tk.Label(
            frame,
            text="Base:"
        ).grid(row=6, column=0, sticky="w", pady=5)

        self.entry_base = ttk.Entry(frame)

        self.entry_base.grid(row=6, column=1, sticky="ew")

        # Sencilla

        tk.Label(
            frame,
            text="Sencilla:"
        ).grid(row=7, column=0, sticky="w", pady=5)

        self.entry_sencilla = ttk.Entry(frame)

        self.entry_sencilla.grid(row=7, column=1, sticky="ew")

        # Monedas

        tk.Label(
            frame,
            text="Monedas:"
        ).grid(row=8, column=0, sticky="w", pady=5)

        self.entry_monedas = ttk.Entry(frame)

        self.entry_monedas.grid(row=8, column=1, sticky="ew")

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

    # ----------------------------
    # GENERAR CIERRE
    # ----------------------------

    def generar_cierre(self):

        try:

            # ----------------------------
            # CAPTURAR ARQUEO
            # ----------------------------

            arqueo = {

                "gruesa": int(
                    self.entry_gruesa.get() or 0
                ),

                "base": int(
                    self.entry_base.get() or 0
                ),

                "sencilla": int(
                    self.entry_sencilla.get() or 0
                ),

                "monedas": int(
                    self.entry_monedas.get() or 0
                )
            }

            # ----------------------------
            # DATOS TEMPORALES
            # ----------------------------

            # Luego esto lo conectarás con Sales

            ventas_sistema = 1000000

            ventas_efectivo = 800000

            utilidad_bruta = 250000

            gastos = []

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

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese solo números"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )