import csv
import os
from datetime import datetime, date
from collections import defaultdict

VENTAS_FILE = "data/ventas.csv"

def guardar_venta(fecha, cantidad, producto, unitario, total):
    """Guarda una venta en el archivo CSV."""
    with open(VENTAS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([fecha, cantidad, producto, unitario, total])


def leer_ventas():
    """Lee todas las ventas desde el archivo CSV."""
    ventas = []
    if os.path.exists(VENTAS_FILE):
        with open(VENTAS_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 5:
                    fecha_str, cantidad, producto, unitario, total = row
                    try:
                        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                        ventas.append({
                            "fecha": fecha,
                            "cantidad": int(cantidad),
                            "producto": producto,
                            "unitario": float(unitario),
                            "total": float(total)
                        })
                    except Exception:
                        pass  # evitar errores por líneas corruptas
    return ventas


def ventas_por_periodo(tipo="dia"):
    """Filtra ventas por tipo: dia, semana, mes, año."""
    hoy = date.today()
    semana_actual = hoy.isocalendar()[1]
    mes_actual = hoy.month
    anio_actual = hoy.year

    total = 0.0
    for venta in leer_ventas():
        fecha = venta["fecha"]

        if tipo == "dia" and fecha == hoy:
            total += venta["total"]
        elif tipo == "semana" and fecha.isocalendar()[1] == semana_actual and fecha.year == anio_actual:
            total += venta["total"]
        elif tipo == "mes" and fecha.month == mes_actual and fecha.year == anio_actual:
            total += venta["total"]
        elif tipo == "anio" and fecha.year == anio_actual:
            total += venta["total"]
    return round(total, 2)


def ventas_del_dia():
    """Devuelve lista de ventas solo del día de hoy."""
    hoy = date.today()
    return [v for v in leer_ventas() if v["fecha"] == hoy]

def productos_mas_vendidos(periodo="dia"):
    hoy = date.today()
    semana = hoy.isocalendar()[1]
    mes = hoy.month
    anio = hoy.year

    resumen = defaultdict(lambda: {"cantidad": 0, "total": 0.0})

    for venta in leer_ventas():
        fecha = venta["fecha"]

        if (
            (periodo == "dia" and fecha == hoy)
            or (periodo == "semana" and fecha.isocalendar()[1] == semana and fecha.year == anio)
            or (periodo == "mes" and fecha.month == mes and fecha.year == anio)
            or (periodo == "anio" and fecha.year == anio)
        ):
            producto = venta["producto"]
            resumen[producto]["cantidad"] += venta["cantidad"]
            resumen[producto]["total"] += venta["total"]

    # Ordenar por cantidad vendida (unidades), no valor
    resultado = sorted(
        [(p, d["cantidad"], d["total"]) for p, d in resumen.items()],
        key=lambda x: x[1],  # ← Cambiado de x[2] a x[1]
        reverse=True
    )


    return resultado