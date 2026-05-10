import csv
import os
import datetime

ARCHIVO = "data/fixes_tecnostyle.csv"


class Repairs:

    @staticmethod
    def registrar_arreglo(cliente, telefono, descripcion, costo, precio):
        fecha = datetime.date.today().isoformat()
        utilidad = precio - costo
        existe = os.path.exists(ARCHIVO)

        with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow([
                    "fecha", "cliente", "telefono",
                    "descripcion", "costo_arreglo",
                    "precio_cliente", "utilidad"
                ])

            writer.writerow([
                fecha, cliente, telefono,
                descripcion, costo, precio, utilidad
            ])

        # 🔁 DEVOLVEMOS datos listos para ventas.csv
        return {
            "fecha": fecha,
            "producto_id": "ARREGLO",
            "nombre": f"Arreglo - {descripcion}",
            "cantidad": 1,
            "costo_unit": costo,
            "precio_unit": precio,
            "descuento": 0,
            "precio_final": precio,
            "total": precio,
            "utilidad": utilidad
        }
