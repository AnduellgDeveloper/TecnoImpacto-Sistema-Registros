import csv
import os

INVENTARIO_FILE = "data/inventario.csv"

class Inventory:
    @staticmethod
    def inicializar():
        """Crea el archivo inventario si no existe"""
        if not os.path.exists(INVENTARIO_FILE):
            with open(INVENTARIO_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "costo", "precio", "stock", "proveedor"])  # 👈 agregado proveedor
                

    @staticmethod
    def cargar_inventario():
        if not os.path.exists(INVENTARIO_FILE):
            Inventory.inicializar()
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            # 👇 Filtramos las líneas que no sean comentarios
            reader = csv.DictReader(row for row in f if not row.startswith("#"))
            return list(reader)


    @staticmethod
    def guardar_inventario(data):
        with open(INVENTARIO_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "nombre", "costo", "precio", "stock", "proveedor"])  # 👈 agregado proveedor
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
    def actualizar_stock(producto_id, cantidad_vendida):
        inventario = Inventory.cargar_inventario()
        for p in inventario:
            if p["id"] == producto_id:
                p["stock"] = str(int(p["stock"]) - cantidad_vendida)
        Inventory.guardar_inventario(inventario)
