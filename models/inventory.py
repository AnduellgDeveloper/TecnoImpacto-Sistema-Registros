import csv
import os

INVENTARIO_FILE = "data/inventario.csv"

class Inventory:
    @staticmethod
    def cargar_inventario():
        if not os.path.exists(INVENTARIO_FILE):
            with open(INVENTARIO_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "costo", "precio", "stock"])
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def guardar_inventario(data):
        with open(INVENTARIO_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "nombre", "costo", "precio", "stock"])
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def agregar_producto(producto):
        inventario = Inventory.cargar_inventario()
        inventario.append(producto)
        Inventory.guardar_inventario(inventario)

    @staticmethod
    def eliminar_producto(producto_id):
        inventario = Inventory.cargar_inventario()
        inventario = [p for p in inventario if p["id"] != producto_id]
        Inventory.guardar_inventario(inventario)

    @staticmethod
    def actualizar_stock(producto_id, cantidad):
        inventario = Inventory.cargar_inventario()
        for p in inventario:
            if p["id"] == producto_id:
                p["stock"] = str(int(p["stock"]) - cantidad)
        Inventory.guardar_inventario(inventario)

    @staticmethod
    def editar_producto(producto_id, nuevo_dato):
        inventario = Inventory.cargar_inventario()
        for p in inventario:
            if p["id"] == producto_id:
                p.update(nuevo_dato)
        Inventory.guardar_inventario(inventario)
