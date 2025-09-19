import csv
import os

PROVEEDORES_FILE = "data/proveedores.csv"

class Providers:
    @staticmethod
    def inicializar():
        if not os.path.exists(PROVEEDORES_FILE):
            with open(PROVEEDORES_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "telefono", "email"])

    @staticmethod
    def cargar_proveedores():
        if not os.path.exists(PROVEEDORES_FILE):
            Providers.inicializar()
        with open(PROVEEDORES_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def guardar_proveedores(data):
        with open(PROVEEDORES_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "nombre", "telefono", "email"])
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def agregar_proveedor(proveedor):
        proveedores = Providers.cargar_proveedores()
        proveedores.append(proveedor)
        Providers.guardar_proveedores(proveedores)

    @staticmethod
    def eliminar_proveedor(proveedor_id):
        proveedores = Providers.cargar_proveedores()
        proveedores = [p for p in proveedores if p["id"] != proveedor_id]
        Providers.guardar_proveedores(proveedores)
