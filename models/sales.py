import csv, os, datetime
from models.inventory import Inventory

VENTAS_FILE = "data/ventas.csv"

class Sales:
    @staticmethod
    def inicializar():
        if not os.path.exists(VENTAS_FILE):
            with open(VENTAS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["fecha", "producto_id", "nombre", "cantidad", "costo_unit", "precio_unit", "utilidad"])

    @staticmethod
    def registrar_venta(producto_id, cantidad):
        inventario = Inventory.cargar_inventario()
        producto = next((p for p in inventario if p["id"] == producto_id), None)

        if producto and int(producto["stock"]) >= cantidad:
            costo = int(producto["costo"])
            precio = int(producto["precio"])
            utilidad = (precio - costo) * cantidad

            with open(VENTAS_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.date.today(),
                    producto_id,
                    producto["nombre"],
                    cantidad,
                    costo,
                    precio,
                    utilidad
                ])

            Inventory.actualizar_stock(producto_id, cantidad)
        else:
            raise ValueError("Stock insuficiente")

    @staticmethod
    def cargar_ventas():
        with open(VENTAS_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def calcular_utilidad(fecha_inicio, fecha_fin):
        ventas = Sales.cargar_ventas()
        utilidad_total = 0
        for v in ventas:
            fecha = datetime.datetime.strptime(v["fecha"], "%Y-%m-%d").date()
            if fecha_inicio <= fecha <= fecha_fin:
                utilidad_total += int(v["utilidad"])
        return utilidad_total
