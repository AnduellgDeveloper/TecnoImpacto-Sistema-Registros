import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Credenciales predefinidas
CREDENTIALS = {
    "admin": "ad123",
    "user": "123"
}

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TecnoImpacto - Ingreso")
        self.master.configure(bg="#ffffff")
        self.master.geometry("400x500")
        self.master.resizable(False, False)

        self.build_interface()

    def build_interface(self):
        # Encabezado con logo
        logo_path = os.path.join("assets", "TecnoImpacto.png")
        if os.path.exists(logo_path):
            image = Image.open(logo_path).resize((250, 150))
            photo = ImageTk.PhotoImage(image)
            self.logo_label = ttk.Label(self.master, image=photo)
            self.logo_label.image = photo
            self.logo_label.pack(pady=10)
        else:
            self.logo_label = ttk.Label(self.master, text="TecnoImpacto", font=("Arial", 18, "bold"))
            self.logo_label.pack(pady=20)

        # Campos de ingreso
        ttk.Label(self.master, text="Usuario:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = ttk.Entry(self.master, width=30)
        self.username_entry.pack()

        ttk.Label(self.master, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = ttk.Entry(self.master, show="*", width=30)
        self.password_entry.pack()

        # Botón de ingreso
        self.login_button = ttk.Button(self.master, text="Ingresar", command=self.verify_credentials)
        self.login_button.pack(pady=20)

    def verify_credentials(self):
        user = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if user in CREDENTIALS and CREDENTIALS[user] == password:
            messagebox.showinfo("Bienvenido", f"Has ingresado como {user}")
            self.master.destroy()
            if user == "admin":
                import views.admin_view as admin
                admin.launch_admin_interface()
            else:
                import views.employee_view as emp
                emp.launch_employee_interface()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
