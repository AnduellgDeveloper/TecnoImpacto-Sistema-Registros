import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import estilos
import difflib


# Diccionario de modelos y medidas
base_vidrios ={
  "Galaxy A10": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Galaxy A10s",
      "Galaxy M10"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G7",
      "Moto G7 Plus",
      "Moto G7 Power"
    ]
  },
  "Galaxy A10s": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Galaxy A10",
      "Galaxy M10"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G7",
      "Moto G7 Plus",
      "Moto G7 Power"
    ]
  },
  "Galaxy A20": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Galaxy A30",
      "Galaxy M20"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G71"
    ]
  },
  "Galaxy A30": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Galaxy A20",
      "Galaxy A50"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G71"
    ]
  },
  "Galaxy A50": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Galaxy A30",
      "Galaxy A30s"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G71"
    ]
  },
  "Galaxy A51": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A71",
      "Galaxy A52"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Galaxy A52": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A52s",
      "Galaxy A51"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Galaxy A52s": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A52",
      "Galaxy A53"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Galaxy A53": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A52s",
      "Galaxy A54"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Galaxy A54": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Galaxy A53",
      "Galaxy A33"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G71"
    ]
  },
  "Galaxy A72": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Galaxy A71",
      "Galaxy A73"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Galaxy A73": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Galaxy A72",
      "Galaxy A71"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Galaxy M12": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A12",
      "Galaxy M21"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Galaxy M21": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Galaxy M31",
      "Galaxy A31"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G71"
    ]
  },
  "Galaxy S20": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Galaxy S21",
      "Galaxy S22"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G7",
      "Moto G7 Plus",
      "Moto G7 Power"
    ]
  },
  "Galaxy S21": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Galaxy S20",
      "Galaxy S22"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G7",
      "Moto G7 Plus",
      "Moto G7 Power"
    ]
  },
  "Galaxy S21 Ultra": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Galaxy S22 Ultra",
      "Galaxy S23 Ultra"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G200",
      "Moto G9 Plus",
      "Moto G9 Power",
      "Moto G Stylus",
      "Moto G Stylus 5G"
    ]
  },
  "Galaxy S22": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "Galaxy S23",
      "Galaxy S21"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XR",
      "iPhone 11",
      "iPhone 12",
      "iPhone 12 Pro",
      "iPhone 13",
      "iPhone 13 Pro",
      "iPhone 14",
      "iPhone 14 Pro",
      "iPhone 15",
      "iPhone 15 Pro",
      "Moto E6s"
    ]
  },
  "Galaxy S23": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "Galaxy S22",
      "Galaxy S24"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone XR",
      "iPhone 11",
      "iPhone 12",
      "iPhone 12 Pro",
      "iPhone 13",
      "iPhone 13 Pro",
      "iPhone 14",
      "iPhone 14 Pro",
      "iPhone 15",
      "iPhone 15 Pro",
      "Moto E6s"
    ]
  },
  "iPhone SE 2020": {
    "medida": "4.7 pulgadas",
    "compatibles": [
      "iPhone 6",
      "iPhone 7",
      "iPhone 8"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 6": {
    "medida": "4.7 pulgadas",
    "compatibles": [
      "iPhone 6s",
      "iPhone 7",
      "iPhone 8"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 6 Plus": {
    "medida": "5.5 pulgadas",
    "compatibles": [
      "iPhone 6s Plus",
      "iPhone 7 Plus",
      "iPhone 8 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6"
    ]
  },
  "iPhone 7": {
    "medida": "4.7 pulgadas",
    "compatibles": [
      "iPhone 6",
      "iPhone 6s",
      "iPhone 8"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 7 Plus": {
    "medida": "5.5 pulgadas",
    "compatibles": [
      "iPhone 6 Plus",
      "iPhone 6s Plus",
      "iPhone 8 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6"
    ]
  },
  "iPhone 8": {
    "medida": "4.7 pulgadas",
    "compatibles": [
      "iPhone 6",
      "iPhone 7",
      "iPhone SE 2020"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 8 Plus": {
    "medida": "5.5 pulgadas",
    "compatibles": [
      "iPhone 6 Plus",
      "iPhone 7 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6"
    ]
  },
  "iPhone X": {
    "medida": "5.8 pulgadas",
    "compatibles": [
      "iPhone XS",
      "iPhone 11 Pro"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone XR": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 11",
      "iPhone 12"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone XS": {
    "medida": "5.8 pulgadas",
    "compatibles": [
      "iPhone X",
      "iPhone 11 Pro"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone XS Max": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "iPhone 11 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "iPhone 11": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone XR",
      "iPhone 12",
      "iPhone 13"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 11 Pro": {
    "medida": "5.8 pulgadas",
    "compatibles": [
      "iPhone XS",
      "iPhone X"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 11 Pro Max": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "iPhone XS Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "Redmi 10",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "iPhone 12 Mini": {
    "medida": "5.4 pulgadas",
    "compatibles": [
      "iPhone 13 Mini"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 12": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 11",
      "iPhone 13"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 12 Pro": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 13 Pro",
      "iPhone 14"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 12 Pro Max": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 13 Pro Max",
      "iPhone 14 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "iPhone 13 Mini": {
    "medida": "5.4 pulgadas",
    "compatibles": [
      "iPhone 12 Mini"
    ],
    "compatibilidad_entre_marcas": []
  },
  "iPhone 13": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 12",
      "iPhone 14"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 13 Pro": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 12 Pro",
      "iPhone 14 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 13 Pro Max": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 12 Pro Max",
      "iPhone 14 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "iPhone 14": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 13",
      "iPhone 12"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 14 Plus": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 13 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "iPhone 14 Pro": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 13 Pro",
      "iPhone 15"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 14 Pro Max": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 13 Pro Max",
      "iPhone 15 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "iPhone 15": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 14",
      "iPhone 13"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 15 Plus": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 14 Plus",
      "iPhone 13 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "iPhone 15 Pro": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "iPhone 14 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "Moto E6s"
    ]
  },
  "iPhone 15 Pro Max": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "iPhone 14 Pro Max",
      "iPhone 13 Pro Max"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Redmi Note 8": {
    "medida": "6.3 pulgadas",
    "compatibles": [
      "Redmi Note 7",
      "Redmi Note 9"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi Note 9": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi 10",
      "Redmi Note 9S"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi Note 11": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "Redmi Note 10",
      "Redmi Note 10S"
    ],
    "compatibilidad_entre_marcas": [
      "OPPO A74",
      "OPPO A95",
      "OPPO Reno 6",
      "OPPO Reno 7"
    ]
  },
  "Redmi Note 12": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Redmi Note 12 Pro",
      "Poco X5"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Redmi Note 12 Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Poco X5",
      "Redmi Note 12"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Redmi Note 10": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "Redmi Note 10S",
      "Redmi Note 11"
    ],
    "compatibilidad_entre_marcas": [
      "OPPO A74",
      "OPPO A95",
      "OPPO Reno 6",
      "OPPO Reno 7"
    ]
  },
  "Redmi Note 10 Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Redmi Note 11 Pro",
      "Poco X3 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Redmi 10": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Redmi 10C",
      "Redmi Note 9"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Motorola One Fusion",
      "Motorola Edge 30",
      "Motorola Moto G13",
      "Moto G14",
      "Moto G20",
      "Moto G30",
      "Moto G50",
      "Moto E20",
      "Moto E30",
      "Moto E40",
      "Moto G22",
      "Moto G23",
      "Moto E7",
      "Moto E7 Plus",
      "Moto G8 Power Lite",
      "Moto G9 Play"
    ]
  },
  "Redmi 10C": {
    "medida": "6.71 pulgadas",
    "compatibles": [
      "Redmi Note 11",
      "Redmi 12C"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi 12C": {
    "medida": "6.71 pulgadas",
    "compatibles": [
      "Redmi 10C",
      "Redmi 10"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi 9": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi Note 9",
      "Redmi 9T"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi 9A": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi 9C",
      "Redmi 9AT"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi 9C": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi 9A",
      "Redmi 9AT"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Redmi 9T": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi 9",
      "Redmi Note 9"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Poco X3": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Poco X3 Pro",
      "Poco X4"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Poco X3 Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Poco X3",
      "Redmi Note 10 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Poco X4 Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Poco X3 Pro",
      "Poco X5"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Poco X5": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Redmi Note 12 Pro",
      "Poco X4 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Poco M3": {
    "medida": "6.53 pulgadas",
    "compatibles": [
      "Redmi 9T",
      "Redmi Note 9"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Poco M4 Pro": {
    "medida": "6.6 pulgadas",
    "compatibles": [
      "Redmi Note 11",
      "Redmi Note 11S"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G82",
      "Infinix Hot 11"
    ]
  },
  "Poco F3": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Redmi K40",
      "Mi 11X"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Poco F4": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Poco F3",
      "Redmi K50"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Mi 10": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Mi 10T",
      "Mi 10T Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Mi 10T": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Mi 10",
      "Mi 10T Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Mi 10T Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Mi 10",
      "Mi 10T"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Mi 11": {
    "medida": "6.81 pulgadas",
    "compatibles": [
      "Mi 11X",
      "Mi 11 Ultra"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Mi 11 Lite": {
    "medida": "6.55 pulgadas",
    "compatibles": [
      "Mi 11 Lite 5G",
      "Xiaomi 11 Lite"
    ],
    "compatibilidad_entre_marcas": [
      "Motorola Edge 40",
      "OPPO Find X5"
    ]
  },
  "Xiaomi 11T": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Xiaomi 11T Pro",
      "Redmi Note 11 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Xiaomi 11T Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Xiaomi 11T",
      "Poco F4"
    ],
    "compatibilidad_entre_marcas": [
      "Infinix Zero X",
      "Infinix Zero X Pro"
    ]
  },
  "Motorola One Fusion": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Motorola One Fusion+",
      "Moto G8 Power Lite"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Motorola Edge 20": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Motorola Edge 20 Pro",
      "Motorola Edge Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Motorola Edge 30": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Motorola Edge 30 Neo",
      "Moto G Stylus 5G"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Motorola Edge 40": {
    "medida": "6.55 pulgadas",
    "compatibles": [
      "Motorola Edge 30",
      "Motorola Edge 40 Neo"
    ],
    "compatibilidad_entre_marcas": [
      "Mi 11 Lite",
      "OPPO Find X5"
    ]
  },
  "Motorola Edge Plus": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Motorola Edge 20",
      "Motorola Edge 30"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Motorola Moto G13": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G23",
      "Moto G32"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G14": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G13",
      "Moto G22"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G20": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G30",
      "Moto G50"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G30": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G20",
      "Moto G50"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G50": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G20",
      "Moto G30"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G100": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Motorola Edge S",
      "Motorola Edge 20"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "OPPO Reno 9",
      "OPPO Find X2",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "Moto G200": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Moto G100",
      "Motorola Edge Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S21 Ultra"
    ]
  },
  "Moto G71": {
    "medida": "6.4 pulgadas",
    "compatibles": [
      "Moto G60",
      "Moto G82"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A20",
      "Galaxy A30",
      "Galaxy A50",
      "Galaxy A54",
      "Galaxy M21"
    ]
  },
  "Moto G82": {
    "medida": "6.6 pulgadas",
    "compatibles": [
      "Moto G71",
      "Motorola Edge 30"
    ],
    "compatibilidad_entre_marcas": [
      "Poco M4 Pro",
      "Infinix Hot 11"
    ]
  },
  "Moto E20": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto E30",
      "Moto E40"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto E30": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto E20",
      "Moto E40"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto E40": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto E20",
      "Moto E30"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G7": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Moto G7 Plus",
      "Moto G7 Power"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A10",
      "Galaxy A10s",
      "Galaxy S20",
      "Galaxy S21"
    ]
  },
  "Moto G7 Plus": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Moto G7",
      "Moto G8 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A10",
      "Galaxy A10s",
      "Galaxy S20",
      "Galaxy S21"
    ]
  },
  "Moto G7 Power": {
    "medida": "6.2 pulgadas",
    "compatibles": [
      "Moto G7",
      "Moto G8 Power"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A10",
      "Galaxy A10s",
      "Galaxy S20",
      "Galaxy S21"
    ]
  },
  "Moto G22": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G13",
      "Moto G23"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G23": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G13",
      "Moto G22"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto E6": {
    "medida": "5.5 pulgadas",
    "compatibles": [
      "Moto E5",
      "Moto E6s"
    ],
    "compatibilidad_entre_marcas": [
      "iPhone 6 Plus",
      "iPhone 7 Plus",
      "iPhone 8 Plus"
    ]
  },
  "Moto E6s": {
    "medida": "6.1 pulgadas",
    "compatibles": [
      "Moto E6",
      "Moto E7"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S22",
      "Galaxy S23",
      "iPhone XR",
      "iPhone 11",
      "iPhone 12",
      "iPhone 12 Pro",
      "iPhone 13",
      "iPhone 13 Pro",
      "iPhone 14",
      "iPhone 14 Pro",
      "iPhone 15",
      "iPhone 15 Pro"
    ]
  },
  "Moto E7": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto E7 Plus",
      "Moto G10"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto E7 Plus": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto E7",
      "Moto G10"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G8 Power Lite": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G9 Play",
      "Motorola One Fusion"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G9 Play": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Moto G8 Power Lite",
      "Moto G9 Plus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A51",
      "Galaxy A52",
      "Galaxy A52s",
      "Galaxy A53",
      "Galaxy M12",
      "iPhone XS Max",
      "iPhone 11 Pro Max",
      "Redmi 10"
    ]
  },
  "Moto G9 Plus": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Moto G9 Power",
      "Moto G Stylus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S21 Ultra"
    ]
  },
  "Moto G9 Power": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Moto G9 Plus",
      "Moto G Stylus"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S21 Ultra"
    ]
  },
  "Moto G Stylus": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Moto G Stylus 5G",
      "Moto G60"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S21 Ultra"
    ]
  },
  "Moto G Stylus 5G": {
    "medida": "6.8 pulgadas",
    "compatibles": [
      "Moto G Stylus",
      "Motorola Edge 30"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy S21 Ultra"
    ]
  },
  "OPPO A15": {
    "medida": "6.52 pulgadas",
    "compatibles": [
      "OPPO A16",
      "OPPO A12"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A17": {
    "medida": "6.56 pulgadas",
    "compatibles": [
      "OPPO A57",
      "OPPO A16k"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A57": {
    "medida": "6.56 pulgadas",
    "compatibles": [
      "OPPO A17",
      "OPPO A16k"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A74": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "OPPO A73",
      "OPPO A54"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 11",
      "Redmi Note 10"
    ]
  },
  "OPPO A76": {
    "medida": "6.56 pulgadas",
    "compatibles": [
      "OPPO A96",
      "OPPO A77"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A96": {
    "medida": "6.59 pulgadas",
    "compatibles": [
      "OPPO A76",
      "OPPO A95"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A95": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "OPPO A74",
      "OPPO A96"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 11",
      "Redmi Note 10"
    ]
  },
  "OPPO Reno 6": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "OPPO Reno 7",
      "OPPO Reno 8"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 11",
      "Redmi Note 10"
    ]
  },
  "OPPO Reno 7": {
    "medida": "6.43 pulgadas",
    "compatibles": [
      "OPPO Reno 6",
      "OPPO Reno 8"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 11",
      "Redmi Note 10"
    ]
  },
  "OPPO Reno 9": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "OPPO Reno 8",
      "OPPO Reno 10"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "OPPO Find X2": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "OPPO Find X3",
      "OPPO Reno 10"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "Infinix Note 11",
      "Infinix Note 12",
      "Infinix Note 12 Pro"
    ]
  },
  "OPPO Find X5": {
    "medida": "6.55 pulgadas",
    "compatibles": [
      "OPPO Find X3",
      "OPPO Find X6"
    ],
    "compatibilidad_entre_marcas": [
      "Mi 11 Lite",
      "Motorola Edge 40"
    ]
  },
  "OPPO Find X6": {
    "medida": "6.74 pulgadas",
    "compatibles": [
      "OPPO Find X5",
      "OPPO Reno 10"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A12": {
    "medida": "6.22 pulgadas",
    "compatibles": [
      "OPPO A15",
      "OPPO A11k"
    ],
    "compatibilidad_entre_marcas": []
  },
  "OPPO A16k": {
    "medida": "6.52 pulgadas",
    "compatibles": [
      "OPPO A16",
      "OPPO A17"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Hot 10": {
    "medida": "6.78 pulgadas",
    "compatibles": [
      "Infinix Hot 11",
      "Infinix Hot 12"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Hot 11": {
    "medida": "6.6 pulgadas",
    "compatibles": [
      "Infinix Hot 10",
      "Infinix Hot 12"
    ],
    "compatibilidad_entre_marcas": [
      "Poco M4 Pro",
      "Moto G82"
    ]
  },
  "Infinix Hot 12": {
    "medida": "6.82 pulgadas",
    "compatibles": [
      "Infinix Hot 11",
      "Infinix Hot 20"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Hot 20": {
    "medida": "6.82 pulgadas",
    "compatibles": [
      "Infinix Hot 12",
      "Infinix Hot 30"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Hot 30": {
    "medida": "6.78 pulgadas",
    "compatibles": [
      "Infinix Hot 20",
      "Infinix Note 30"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Zero 8": {
    "medida": "6.85 pulgadas",
    "compatibles": [
      "Infinix Zero 9",
      "Infinix Note 10"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Zero 9": {
    "medida": "6.85 pulgadas",
    "compatibles": [
      "Infinix Zero 8",
      "Infinix Zero X"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Zero X": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Infinix Zero X Pro",
      "Infinix Zero 9"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 12",
      "Redmi Note 12 Pro",
      "Redmi Note 10 Pro",
      "Poco X3",
      "Poco X3 Pro",
      "Poco X4 Pro",
      "Poco X5",
      "Poco F3",
      "Poco F4",
      "Mi 10",
      "Mi 10T",
      "Mi 10T Pro",
      "Xiaomi 11T",
      "Xiaomi 11T Pro"
    ]
  },
  "Infinix Zero X Pro": {
    "medida": "6.67 pulgadas",
    "compatibles": [
      "Infinix Zero X",
      "Infinix Zero 5G"
    ],
    "compatibilidad_entre_marcas": [
      "Redmi Note 12",
      "Redmi Note 12 Pro",
      "Redmi Note 10 Pro",
      "Poco X3",
      "Poco X3 Pro",
      "Poco X4 Pro",
      "Poco X5",
      "Poco F3",
      "Poco F4",
      "Mi 10",
      "Mi 10T",
      "Mi 10T Pro",
      "Xiaomi 11T",
      "Xiaomi 11T Pro"
    ]
  },
  "Infinix Zero 5G": {
    "medida": "6.78 pulgadas",
    "compatibles": [
      "Infinix Zero X Pro",
      "Infinix Note 12 Pro"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Note 10": {
    "medida": "6.95 pulgadas",
    "compatibles": [
      "Infinix Note 11",
      "Infinix Note 12"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Note 11": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Infinix Note 10",
      "Infinix Note 12i"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2"
    ]
  },
  "Infinix Note 12": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Infinix Note 11",
      "Infinix Note 12 Pro"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2"
    ]
  },
  "Infinix Note 12i": {
    "medida": "6.82 pulgadas",
    "compatibles": [
      "Infinix Note 12",
      "Infinix Hot 20"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Note 12 Pro": {
    "medida": "6.7 pulgadas",
    "compatibles": [
      "Infinix Note 12",
      "Infinix Zero 5G"
    ],
    "compatibilidad_entre_marcas": [
      "Galaxy A72",
      "Galaxy A73",
      "iPhone 12 Pro Max",
      "iPhone 13 Pro Max",
      "iPhone 14 Plus",
      "iPhone 14 Pro Max",
      "iPhone 15 Plus",
      "iPhone 15 Pro Max",
      "Motorola Edge 20",
      "Motorola Edge Plus",
      "Moto G100",
      "OPPO Reno 9",
      "OPPO Find X2"
    ]
  },
  "Infinix Note 30": {
    "medida": "6.78 pulgadas",
    "compatibles": [
      "Infinix Hot 30",
      "Infinix Zero 30"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Infinix Zero 30": {
    "medida": "6.78 pulgadas",
    "compatibles": [
      "Infinix Note 30",
      "Infinix Zero 5G"
    ],
    "compatibilidad_entre_marcas": []
  },
  "Galaxy A02": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A02s",
      "Galaxy A03"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E20",
      "Moto E30",
      "Redmi 10"
    ]
  },
  "Galaxy A02s": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A02",
      "Galaxy A03s"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E20",
      "Moto G9 Play"
    ]
  },
  "Galaxy A03": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A02",
      "Galaxy A03 Core"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E30",
      "Redmi 9A"
    ]
  },
  "Galaxy A03s": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A02s",
      "Galaxy A04s"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G13",
      "Redmi 10C"
    ]
  },
  "Galaxy A04s": {
    "medida": "6.5 pulgadas",
    "compatibles": [
      "Galaxy A03s",
      "Galaxy A14"
    ],
    "compatibilidad_entre_marcas": [
      "Moto G13",
      "Redmi 10C"
    ]
  },
  "Galaxy A01": {
    "medida": "5.7 pulgadas",
    "compatibles": [
      "Galaxy A01 Core",
      "Galaxy M01"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6",
      "Redmi 7A"
    ]
  },
  "Galaxy A01 Core": {
    "medida": "5.3 pulgadas",
    "compatibles": [
      "Galaxy A01",
      "Galaxy M01 Core"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6"
    ]
  },
  "Galaxy M01": {
    "medida": "5.7 pulgadas",
    "compatibles": [
      "Galaxy A01",
      "Galaxy A01 Core"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6s"
    ]
  },
  "Galaxy M01 Core": {
    "medida": "5.3 pulgadas",
    "compatibles": [
      "Galaxy A01 Core",
      "Galaxy A01"
    ],
    "compatibilidad_entre_marcas": [
      "Moto E6"
    ]
  }
}



# Construcción del diccionario invertido
modelo_index = {}

for modelo, datos in base_vidrios.items():
    modelo_index[modelo] = {
        "medida": datos["medida"],
        "modelo_principal": modelo,
        "compatibles": datos["compatibles"],
        "compatibilidad_entre_marcas": datos.get("compatibilidad_entre_marcas", [])
    }
    for comp in datos["compatibles"]:
        if comp not in modelo_index:
            modelo_index[comp] = {
                "medida": datos["medida"],
                "modelo_principal": modelo,
                "compatibles": datos["compatibles"],
                "compatibilidad_entre_marcas": datos.get("compatibilidad_entre_marcas", [])
            }


# Función de búsqueda universal (directa o inversa)
def buscar_modelo():
    modelo_usuario = entry_modelo.get().strip()
    resultado = modelo_index.get(modelo_usuario)

    if not resultado:
        sugerencias = difflib.get_close_matches(modelo_usuario, modelo_index.keys(), n=1, cutoff=0.6)
        if sugerencias:
            modelo_sugerido = sugerencias[0]
            resultado = modelo_index[modelo_sugerido]
            etiqueta_resultado.config(
                text=f"📱 Modelo buscado (coincidencia aproximada): {modelo_usuario}\n"
                     f"🔰 Modelo encontrado: {modelo_sugerido}\n"
                     f"📐 Medida del vidrio: {resultado['medida']}\n"
                     f"🔁 Compatibles: {', '.join(resultado['compatibles']) or 'Ninguno'}\n"
                     f"🔁 Compatibles entre marcas: {', '.join(resultado['compatibilidad_entre_marcas']) or 'Ninguno'}"
            )
        else:
            etiqueta_resultado.config(text="❌ Modelo no encontrado. Verifica el nombre.")
            messagebox.showinfo("Modelo no encontrado", "Ese modelo no está en la base de datos.")
    else:
        etiqueta_resultado.config(
            text=f"📱 Modelo buscado: {modelo_usuario}\n"
                 f"🔰 Modelo principal: {resultado['modelo_principal']}\n"
                 f"📐 Medida del vidrio: {resultado['medida']}\n"
                 f"🔁 Compatibles: {', '.join(resultado['compatibles']) or 'Ninguno'}\n"
                 f"🔁 Compatibles entre marcas: {', '.join(resultado['compatibilidad_entre_marcas']) or 'Ninguno'}"
        )

# Interfaz
ventana = tk.Tk()
ventana.title("Gestión de Vidrios Templados")
ventana.geometry("500x450")
ventana.configure(bg=estilos.COLOR_FONDO)

# Logo
try:
    imagen_logo = Image.open("TecnoImpacto.png")
    imagen_logo = imagen_logo.resize((410, 180))
    logo = ImageTk.PhotoImage(imagen_logo)
    label_logo = tk.Label(ventana, image=logo, bg=estilos.COLOR_FONDO)
    label_logo.pack(pady=5)
except:
    label_logo = tk.Label(ventana, text="", font=estilos.FUENTE_TITULO, bg=estilos.COLOR_FONDO, fg=estilos.COLOR_SECUNDARIO)
    label_logo.pack(pady=10)

# Entrada
frame_busqueda = tk.Frame(ventana, bg=estilos.COLOR_FONDO)
frame_busqueda.pack(pady=15)

tk.Label(frame_busqueda, text="🔍 Ingrese modelo de celular:", font=estilos.FUENTE_NORMAL, bg=estilos.COLOR_FONDO, fg=estilos.COLOR_TEXTO).grid(row=0, column=0, padx=5)
entry_modelo = tk.Entry(frame_busqueda, width=30, bg=estilos.COLOR_ENTRADA, font=estilos.FUENTE_NORMAL)
entry_modelo.grid(row=0, column=1)

btn_buscar = tk.Button(ventana, text="Buscar", command=buscar_modelo,
                       bg=estilos.COLOR_BOTON, fg=estilos.COLOR_BOTON_TEXTO, font=estilos.FUENTE_NORMAL)
btn_buscar.pack(pady=5)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", font=estilos.FUENTE_NORMAL,
                              justify="left", wraplength=450, bg=estilos.COLOR_FONDO, fg=estilos.COLOR_TEXTO)
etiqueta_resultado.pack(pady=10)

ventana.mainloop()