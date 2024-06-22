import tkinter as tk

class FormularioLibrosDesign:

    def __init__(self, parent, biblioteca):
        self.mostrar_lista_libros()
        self.parent = parent
        self.biblioteca = biblioteca

        self.crear_widgets()
    def crear_widgets(self):
        # Crear el título
        self.label_titulo = tk.Label(self.parent, text="Lista de Libros", font=("Helvetica", 16, "bold"))
        self.label_titulo.pack(pady=10)

        # Crear el frame para el cuadro de texto de libros
        self.frame_libros = tk.Frame(self.parent)
        self.frame_libros.pack(fill='both', expand=True, padx=20, pady=10)

        # Crear un scrollbar para el frame
        self.scrollbar = tk.Scrollbar(self.frame_libros)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear el Cuadro de Texto para mostrar los libros
        self.textbox_libros = tk.Text(self.frame_libros, yscrollcommand=self.scrollbar.set, font=("Helvetica", 12))
        self.textbox_libros.pack(side=tk.LEFT, fill='both', expand=True)
        self.scrollbar.config(command=self.textbox_libros.yview)

        # Llenar el Cuadro de Texto con los libros de la biblioteca
        self.llenar_texto_libros()

    def llenar_texto_libros(self):
        for libro in self.biblioteca._libros:
            info_libro = f"Título: {libro.get_titulo()}\nISBN: {libro.get_isbn()}\nAutor: {libro.get_autor().get_nombre()} {libro.get_autor().get_apellido()}\nCategoría: {libro.get_categoria().get_nombre()}\n\n"
            self.textbox_libros.insert(tk.END, info_libro)

