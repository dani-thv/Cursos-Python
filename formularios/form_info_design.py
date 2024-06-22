import tkinter as tk
import util.util_ventana as util_ventana

class FormularioInfoDesign(tk.Toplevel):

    def __init__(self) -> None:
        super().__init__()
        self.config_window()
        self.contruirWidget()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Biblioteca')
        self.iconbitmap("./imagenes/R.ico")
        w, h = 400, 100        
        util_ventana.centrar_ventana(self, w, h)     
    
    def contruirWidget(self):         
        self.labelVersion = tk.Label(self, text="Version : 1.0")
        self.labelVersion.config(fg="#000000", font=(
            "Roboto", 15), pady=10, width=20)
        self.labelVersion.pack()

        self.labelAutor = tk.Label(self, text="Autor : Jesús Gutiérrez")
        self.labelAutor.config(fg="#000000", font=(
            "Roboto", 15), pady=10, width=20)
        self.labelAutor.pack()


