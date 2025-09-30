import tkinter as tk
from tkinter import messagebox, ttk

class FrmEstudiantes:
    def __init__(self, root):
        self.root = root
        self.root.title("FrmEstudiantes")
        self.root.geometry("500x500")

        self.datos = {}

        tk.Label(root, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
        self.txt_nombre = tk.Entry(root)
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Apellido").grid(row=1, column=0, padx=10, pady=5)
        self.txt_apellido = tk.Entry(root)
        self.txt_apellido.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad").grid(row=2, column=0, padx=10, pady=5)
        self.txt_edad = tk.Entry(root)
        self.txt_edad.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Teléfono").grid(row=3, column=0, padx=10, pady=5)
        self.txt_telefono = tk.Entry(root)
        self.txt_telefono.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Correo").grid(row=4, column=0, padx=10, pady=5)
        self.txt_correo = tk.Entry(root)
        self.txt_correo.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Asignatura").grid(row=5, column=0, padx=10, pady=5)
        self.cmb_asignatura = ttk.Combobox(root, values=["Matemáticas", "Lengua", "Historia", "Ciencias", "Inglés"])
        self.cmb_asignatura.grid(row=5, column=1, padx=10, pady=5)

        self.btn_guardar = tk.Button(root, text="Guardar", command=self.guardar)
        self.btn_guardar.grid(row=6, column=0, padx=10, pady=10)

        self.btn_listar = tk.Button(root, text="Listar", command=self.listar)
        self.btn_listar.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(root, text="Datos almacenados:").grid(row=7, column=0, columnspan=2)
        self.txt_resultado = tk.Text(root, height=10, width=50)
        self.txt_resultado.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def guardar(self):
        nombre = self.txt_nombre.get()
        apellido = self.txt_apellido.get()
        edad = self.txt_edad.get()
        telefono = self.txt_telefono.get()
        correo = self.txt_correo.get()
        asignatura = self.cmb_asignatura.get()

        if not nombre or not apellido:
            messagebox.showwarning("Aviso", "Nombre y Apellido son obligatorios")
            return

        self.datos[nombre] = f"{apellido}, {edad}, {telefono}, {correo}, {asignatura}"

        self.txt_nombre.delete(0, tk.END)
        self.txt_apellido.delete(0, tk.END)
        self.txt_edad.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)
        self.txt_correo.delete(0, tk.END)
        self.cmb_asignatura.set("")

        messagebox.showinfo("Éxito", "Datos guardados correctamente")

    def listar(self):
        self.txt_resultado.delete("1.0", tk.END)
        for nombre, datos in self.datos.items():
            self.txt_resultado.insert(tk.END, f"{nombre}: {datos}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrmEstudiantes(root)
    root.mainloop()