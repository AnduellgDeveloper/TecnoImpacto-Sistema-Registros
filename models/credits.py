import csv
import os
import datetime
import json

ARCHIVO = "data/creditos.csv"

class Credits:

    @staticmethod
    def registrar_credito(data):
        """
        data = {
            fecha, cliente, telefono,
            productos (lista),
            credito_celular,
            total, valor_85, valor_15,
            cuotas, valor_recibido, saldo
        }
        """
        existe = os.path.exists(ARCHIVO)

        with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow([
                    "fecha", "cliente", "telefono",
                    "productos", "credito_celular",
                    "total", "valor_85", "valor_15",
                    "cuotas", "valor_recibido", "saldo"
                ])

            writer.writerow([
                data["fecha"],
                data["cliente"],
                data["telefono"],
                json.dumps(data["productos"], ensure_ascii=False),
                data["credito_celular"],
                data["total"],
                data["valor_85"],
                data["valor_15"],
                data["cuotas"],
                data["valor_recibido"],
                data["saldo"]
            ])
