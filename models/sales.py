import csv
import os
import datetime
from models.inventory import Inventory
from collections import Counter
VENTAS_FILE = "data/ventas.csv"


class Sales:
    @staticmethod
    def inicializar():
        """Crea el archivo de ventas si no existe con los encabezados correctos"""
        if not os.path.exists(VENTAS_FILE):
            with open(VENTAS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "fecha", "producto_id", "nombre", "cantidad",
                    "costo_unit", "precio_unit",
                    "descuento", "precio_final", "total", "utilidad"
                ])

    @staticmethod
    def registrar_venta(producto_id, cantidad, descuento=0):
        """Registra una venta en el CSV aplicando descuento"""
        inventario = Inventory.cargar_inventario()
        producto = next((p for p in inventario if p["id"] == producto_id), None)

        if producto and int(producto["stock"]) >= cantidad:
            costo = int(producto["costo"])
            precio = int(producto["precio"])
            precio_final = max(precio - descuento, 0)
            total = precio_final * cantidad
            utilidad = (precio_final - costo) * cantidad

            with open(VENTAS_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.date.today(),
                    producto_id,
                    producto["nombre"],
                    cantidad,
                    costo,
                    precio,
                    descuento,
                    precio_final,
                    total,
                    utilidad
                ])

            Inventory.actualizar_stock(producto_id, cantidad)
        else:
            raise ValueError("Stock insuficiente")

    @staticmethod
    def cargar_ventas():
        """Carga todas las ventas desde el CSV"""
        with open(VENTAS_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def calcular_utilidad(fecha_inicio, fecha_fin):
        """Calcula la utilidad entre dos fechas"""
        ventas = Sales.cargar_ventas()
        utilidad_total = 0
        for v in ventas:
            fecha = datetime.datetime.strptime(v["fecha"], "%Y-%m-%d").date()
            if fecha_inicio <= fecha <= fecha_fin:
                utilidad_total += int(v["utilidad"])
        return utilidad_total
    
    @staticmethod
    def calcular_ventas(fecha_inicio, fecha_fin):
        """Calcula el total de ventas entre dos fechas"""
        ventas = Sales.cargar_ventas()
        ventas_total = 0
        for v in ventas:
            fecha = datetime.datetime.strptime(v["fecha"], "%Y-%m-%d").date()
            if fecha_inicio <= fecha <= fecha_fin:
                ventas_total += int(v["total"])
        return ventas_total

    @staticmethod
    def productos_mas_vendidos(fecha_inicio, fecha_fin, top=10):
        """Retorna los productos más vendidos en un rango de fechas"""
        ventas = Sales.cargar_ventas()
        contador = Counter()
        for v in ventas:
            fecha = datetime.datetime.strptime(v["fecha"], "%Y-%m-%d").date()
            if fecha_inicio <= fecha <= fecha_fin:
                contador[v["nombre"]] += int(v["cantidad"])
        return contador.most_common(top)