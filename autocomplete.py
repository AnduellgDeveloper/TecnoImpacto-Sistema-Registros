import tkinter as tk

class AutocompleteEntry(tk.Entry):
    def __init__(self, palabras_clave, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.palabras_clave = palabras_clave
        self.sugerencias = []
        self.lb = None

        self.bind("<KeyRelease>", self.check_sugerencias)

    def check_sugerencias(self, event=None):
        texto = self.get().lower()
        self.sugerencias = []

        for clave, opciones in self.palabras_clave.items():
            if clave in texto:
                self.sugerencias.extend(opciones)

        if self.sugerencias:
            self.show_suggestions()
        else:
            self.hide_suggestions()

    def show_suggestions(self):
        if self.lb:
            self.lb.destroy()

        # Crear ventana flotante para sugerencias
        self.lb = tk.Toplevel(self)
        self.lb.overrideredirect(True)  # sin bordes
        self.lb.geometry(f"{self.winfo_width()}x100+{self.winfo_rootx()}+{self.winfo_rooty() + self.winfo_height()}")

        listbox = tk.Listbox(self.lb, height=min(5, len(self.sugerencias)))
        listbox.pack(fill="both", expand=True)

        for item in self.sugerencias:
            listbox.insert(tk.END, item)

        listbox.bind("<<ListboxSelect>>", lambda e: self.autocompletar(e, listbox))

    def hide_suggestions(self):
        if self.lb:
            self.lb.destroy()
            self.lb = None

    def autocompletar(self, event, listbox):
        seleccion = listbox.curselection()
        if seleccion:
            texto = listbox.get(seleccion)
            self.delete(0, tk.END)
            self.insert(0, texto)
        self.hide_suggestions()
        self.focus_set()

