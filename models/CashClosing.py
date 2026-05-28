import json
import os
import datetime

class CashClosing:

    FILE = "data/closings.json"

    # Carga los cierres de caja desde el archivo JSON, devuelve una lista de cierres
    @staticmethod
    def cargar_cierres():

        if not os.path.exists(CashClosing.FILE):
            return []

        try:

            with open(
                CashClosing.FILE,
                "r",
                encoding="utf-8"
            ) as file:

                contenido = file.read().strip()

                if not contenido:
                    return []

                return json.loads(contenido)

        except:

            return []
        
    # Guarda y agrega un nuevo cierre de caja a la lista de cierres y lo guarda en el archivo JSON
    @staticmethod
    def guardar_cierres(cierres):

        with open(CashClosing.FILE, "w", encoding="utf-8") as file:
            json.dump(cierres, file, indent=4, ensure_ascii=False)
    
    # Validar solo un cierre de caja al día
    @staticmethod
    def existe_cierre(fecha):

        cierres = CashClosing.cargar_cierres()

        for cierre in cierres:

            if cierre["fecha"] == fecha:
                return True

        return False        


    @staticmethod
    def calcular_total_gastos(gastos):

        total = 0

        for gasto in gastos:
            total += gasto["valor"]

        return total
    

    @staticmethod
    def calcular_gastos_caja(gastos):

        total = 0

        for gasto in gastos:

            if gasto["afecta_caja"]:
                total += gasto["valor"]

        return total
    
    @staticmethod
    def calcular_utilidad_neta(utilidad_bruta, gastos):

        total_gastos = CashClosing.calcular_total_gastos(gastos)

        return utilidad_bruta - total_gastos
    
    @staticmethod
    def calcular_caja_esperada(
        ventas_efectivo,
        gastos
    ):

        gastos_caja = CashClosing.calcular_gastos_caja(gastos)

        return ventas_efectivo - gastos_caja
    

    @staticmethod
    def calcular_diferencia(
        caja_real,
        caja_esperada
    ):

        return caja_real - caja_esperada
    
    @staticmethod
    def calcular_caja_real(arqueo):

        total = 0
        total += arqueo.get("gruesa", 0)
        total += arqueo.get("base", 0)
        total += arqueo.get("sencilla", 0)
        total += arqueo.get("monedas", 0)

        return total
    
    arqueo = {
    "gruesa": 450000,
    "base": 280000,
    "sencilla": 68000,
    "monedas": 12500
    }

    @staticmethod
    def generar_cierre(
        ventas_sistema,
        ventas_efectivo,
        utilidad_bruta,
        gastos,
        arqueo
    ):
        
     # Fecha actual
        fecha = str(datetime.date.today())

        # Validar cierre único
        if CashClosing.existe_cierre(fecha):

            raise Exception(
                "Ya existe un cierre hoy"
            )

        # Calcular caja real
        caja_real = CashClosing.calcular_caja_real(arqueo)

        # Calcular caja esperada
        caja_esperada = CashClosing.calcular_caja_esperada(
            ventas_efectivo,
            gastos
        )

        # Calcular diferencia
        diferencia = CashClosing.calcular_diferencia(
            caja_real,
            caja_esperada
        )

        # Calcular utilidad neta
        utilidad_neta = CashClosing.calcular_utilidad_neta(
            utilidad_bruta,
            gastos
        )

        # Crear objeto cierre
        cierre = {

            "fecha": fecha,

            "ventas_sistema": ventas_sistema,
            "ventas_efectivo": ventas_efectivo,
            "utilidad_bruta": utilidad_bruta,
            "gastos": gastos,
            "arqueo": arqueo,
            "caja_real": caja_real,
            "caja_esperada": caja_esperada,
            "diferencia": diferencia,
            "utilidad_neta": utilidad_neta
        }

        # Guardar cierre
        cierres = CashClosing.cargar_cierres()

        cierres.append(cierre)

        CashClosing.guardar_cierres(cierres)

        # Retornar resultado
        return cierre
        

           