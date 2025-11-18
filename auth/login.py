import tkinter as tk
from tkinter import ttk, messagebox
from views.admin_view import AdminView
from views.employee_view import EmployeeView


def centrar_ventana(ventana, ancho, alto):
    """Centra la ventana en la pantalla"""
    ventana.update_idletasks()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ancho // 2)
    y = (screen_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

class LoginApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema TecnoImpacto - Login")

        centrar_ventana(self.root, 450, 320)
        self.root.configure(bg="#f0f0f0")
        
        frame = tk.Frame(root, bg="white", bd=2, relief="groove")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=220)

        title = tk.Label(frame, text="Iniciar Sesión", font=("Arial", 14, "bold"), bg="white")
        title.pack(pady=10)

        tk.Label(frame, text="Usuario:", font=("Arial", 11), bg="white").pack(pady=5)
        self.username_entry = ttk.Entry(frame, font=("Arial", 11))
        self.username_entry.pack()

        tk.Label(frame, text="Contraseña:", font=("Arial", 11), bg="white").pack(pady=5)
        self.password_entry = ttk.Entry(frame, show="*", font=("Arial", 11))
        self.password_entry.pack()

        login_btn = ttk.Button(frame, text="Ingresar", command=self.verify_credentials)
        login_btn.pack(pady=15)

    


    def verify_credentials(self):
        user = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if user == "admin" and password == "7777":
            new_window = tk.Toplevel(self.root)
            AdminView(new_window)
        elif user == "user" and password == "123":
            new_window = tk.Toplevel(self.root)
            EmployeeView(new_window)
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
