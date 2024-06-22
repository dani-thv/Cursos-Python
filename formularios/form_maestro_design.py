import datetime
import sqlite3
import tkinter as tk
from tkinter import Image, PhotoImage, font
from tkinter import messagebox
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import ImageTk, Image


class Profesor:  # Creacion de la clase profesor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        print("Nombre del profesor:", self.nombre, self.apellido)

    # Getter y setter para el nombre del profesor
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Getter y setter para el apellido del profesor
    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

class Usuario:#clase usuario
    def __init__(self, nombre, apellido, id_user): 
        self._nombre = nombre
        self._apellido = apellido
        self._id_user = id_user

    def get_nombre(self):  # metodo para obtener el nombre del usuario
        return self._nombre

    def get_apellido(self):  # metodo para obtener el apellido del usuario
        return self._apellido

    def get_id_user(self):  # metodo para obtener el id del usuario
        return self._id_user

    #setters

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_id_user(self, id_user ):
        self._id_user  = id_user

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

 #getter
    def get_dia(self):
        return self._dia

    def get_hora_inicio(self):
        return self._hora_inicio

    def get_hora_fin(self):
        return self._hora_fin

#setters
    def set_dia(self, dia):
        self._dia = dia

    def set_hora_inicio(self, hora_inicio):
        self._hora_inicio = hora_inicio

    def set_hora_fin(self, hora_fin):
        self._hora_fin = hora_fin

    def mostrar_info(self):
        print(f"Horario: {self._dia}, de {self._hora_inicio} a {self._hora_fin}")

class Evaluacion:
    def __init__(self, usuario, nota):
        self.usuario = usuario
        self.nota = nota

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota

    def get_usuario(self): #metodo para obtener el usuario que realizara el prestamo
        return self.usuario

    def mostrar_info(self):
        print("Estudiante:", self.usuario.nombre, self.usuario.apellido)
        print("Nota:", self.nota)

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        print("Nombre de la asignatura:", self.nombre)
        print("Profesor:", self.profesor.nombre, self.profesor.apellido)

    def get_nombre(self):
        return self.nombre
    
    def get_profesor(self):
        return self.profesor

class Grupo:
    def __init__(self, nombre, asignatura, horario, usuario):
        self.nombre= nombre
        self.asignatura = asignatura 
        self.horario = horario
        self.usuario = usuario
    
    def mostrar_info(self):
        print("Grupo:", self.nombre)
        print("Asignatura:", self.asignatura.nombre, self.asignatura.get_profesor().get_nombre().get_apellido())
        print("Horario:", self.horario.mostrar_info())
        print("Estudiantes:", self.usuario.mostrar_info())
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_asignatura(self):
        return self.asignatura
    
    def get_horario(self):
        return self.horario
    
    def get_usuario(self):
        return self.usuario

class Curso:
    def __init__(self):
        self.asignaturas = []
        self.profesores = []
        self.horarios = []
        self.evaluaciones = []
        self.grupos= []

    def registrar_asignaturas(self, asignatura): #metodo para realizar el registro de usuarios a la biblioteca
        self.asignaturas.append(asignatura)

    def registrar_horarios(self, horario):
        self.horarios.append(horario)

    def registrar_evaluaciones(self, evaluacion):
        self.evaluaciones.append(evaluacion)
    
    def registrar_grupos(self, grupo):
        self.grupos.append(grupo)

    def mostrar_evas(self): #metodo para mostrar los libros de la biblioteca
        for evaluacion in self.evaluaciones:
            evaluacion.mostrar_info()

    def mostrar_asignaturas(self): #metodo para mostrar los libros de la biblioteca
        for asignatura in self.asignaturas:
            asignatura.mostrar_info()

    def mostrar_horario(self):
        for horario in self.horarios:
            horario.mostrar_info()

    def buscar_grupo_por_nombre(self, nombre):
        for grupo in self.grupos:
            if grupo.get_nombre().lower() == nombre.lower():
                return grupo
        return None

class LoginWindow(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Login")
        self.geometry("1500x1500")
        self.crear_widgets()

        # Conectar a la base de datos SQLite
        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()
        

        self.curso = Curso() 
        # Lista de usuarios predefinidos

        usuarios = [
            Usuario("Pedro", "Gomez", "001"),
            Usuario("Ana", "Martinez", "002"),
            Usuario("Luis", "Rodriguez", "003"),
            Usuario("Laura", "Diaz", "004"),
            Usuario("Carlos", "Lopez", "005"),
            Usuario("Sofia", "Sanchez", "006"),
            Usuario("Diego", "Hernandez", "007"),
            Usuario("Valentina", "Perez", "008"),
            Usuario("Andres", "Gutierrez", "009"),
            Usuario("Juliana", "Gomez", "010")
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

        profesores = [
            Profesor("Juan", "Perez"),
            Profesor("Isabela", "Garcia"),
            Profesor("Maria", "Gonzalez")
        ]

        asignaturas = [
            Asignatura("Matemáticas", profesores[0]),
            Asignatura("Física", profesores[1]),
            Asignatura("Mecánica", profesores[2])
        ]

        for asignatura in asignaturas:
            self.curso.registrar_asignaturas(asignatura)

        horarios = [
            Horario("Lunes", "08:00", "10:00"),
            Horario("Martes", "10:00", "12:00")
        ]

        for horario in horarios:
            self.curso.registrar_horarios(horario)

        evaluaciones = [
            Evaluacion(usuarios[0], 3.8),
            Evaluacion(usuarios[1], 4.5)
        ]
        for evaluacion in evaluaciones:
            self.curso.registrar_evaluaciones(evaluacion)

        grupos = [
        Grupo("DR", asignaturas[1], Horario("Lunes", "08:00", "10:00"), usuarios[4]),
        Grupo("BR", asignaturas[2], Horario("Martes", "10:00", "12:00"), usuarios[2])
        ]
        for grupo in grupos:
            self.curso.registrar_grupos(grupo)


    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def registrar_usuario(self, usuario):
        self.cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", 
                            (usuario.get_id_user(), usuario.get_nombre(), usuario.get_apellido()))
        self.conexion.commit()

    def crear_widgets(self):
        # Título
        self.label = tk.Label(self, text="Universidad de Pamplona", fg="black", font=("Helvetica", 22))
        self.label.pack(pady=20)

        # Imagen
        ruta_imagen = "./imagenes/leon.png"
        imagen = PhotoImage(file=ruta_imagen)
        imagen_redimensionada = imagen.subsample(5, 5)
        etiqueta_imagen = tk.Label(self, image=imagen_redimensionada)
        etiqueta_imagen.image = imagen_redimensionada
        etiqueta_imagen.pack()

        # Bienvenida
        self.label_bienvenida = tk.Label(self, text="Bienvenido, digite sus datos en los siguientes campos para acceder al sistema.", fg="black", font=("Helvetica", 16))
        self.label_bienvenida.pack(pady=20)

        # Campos de entrada
        self.label_nombre = tk.Label(self, text="Nombre:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        self.label_apellido = tk.Label(self, text="Apellido:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_apellido.pack(pady=5)
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.pack(pady=5)

        self.label_id = tk.Label(self, text="ID:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=5)

        # Botones
        self.btn_iniciar_sesion = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.btn_iniciar_sesion.pack(pady=5)

        self.label_registro = tk.Label(self, text="¿Eres nuevo? Regístrate", bg="Light Yellow", fg="black", font=("Helvetica", 16))
        self.label_registro.pack(pady=15)

        self.btn_crear_usuario = tk.Button(self, text="Crear Usuario", command=self.abrir_ventana_crear_usuario)
        self.btn_crear_usuario.pack(pady=5)

        self.boton_salir = tk.Button(self, text="Salir", command=self.destroy, bg="#f44336", fg="#ffffff", relief=tk.FLAT)
        self.boton_salir.pack(pady=10)

    def iniciar_sesion(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        id_usuario = self.entry_id.get()
        
        self.cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND apellido = ? AND id = ?", (nombre, apellido, id_usuario))
        resultado = self.cursor.fetchone()
        
        if resultado:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
        # Ocultar la ventana principal y mostrar la ventana de opciones
            self.parent.show_main_window()  # Llamar al método para mostrar la ventana principal
            self.destroy()
        else:
            messagebox.showerror("Error", "Nombre, apellido o ID incorrectos")

    def abrir_ventana_crear_usuario(self):
        ventana_crear_usuario = CrearUsuarioWindow(self)
        ventana_crear_usuario.grab_set()

class CrearUsuarioWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear Usuario")
        self.geometry("400x300")
        self.configure(bg="light blue")
        self.crear_widgets()
        self.usuarios = []
    
        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()

        usuarios = [
            Usuario("Pedro", "Gomez", "001"),
            Usuario("Ana", "Martinez", "002"),
            Usuario("Luis", "Rodriguez", "003"),
            Usuario("Laura", "Diaz", "004"),
            Usuario("Carlos", "Lopez", "005"),
            Usuario("Sofia", "Sanchez", "006"),
            Usuario("Diego", "Hernandez", "007"),
            Usuario("Valentina", "Perez", "008"),
            Usuario("Andres", "Gutierrez", "009"),
            Usuario("Juliana", "Gomez", "010")
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def crear_usuario(self):
        nombre = self.entry_nuevo_nombre.get()
        apellido = self.entry_nuevo_apellido.get()
        id_usuario = self.entry_nuevo_id.get()

        if id_usuario and nombre and apellido:
            try:
                self.cursor.execute("INSERT INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", (id_usuario, nombre, apellido))
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario creado con éxito")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El ID de usuario ya existe")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el usuario: {e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")



    def crear_widgets(self):

        self.label_nuevo_nombre = tk.Label(self, text="Nombre:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_nombre.pack(pady=5)
        self.entry_nuevo_nombre = tk.Entry(self)
        self.entry_nuevo_nombre.pack(pady=5)

        self.label_nuevo_apellido = tk.Label(self, text="Apellido:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_apellido.pack(pady=5)
        self.entry_nuevo_apellido = tk.Entry(self)
        self.entry_nuevo_apellido.pack(pady=5)

        self.label_nuevo_id = tk.Label(self, text="ID:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_id.pack(pady=5)
        self.entry_nuevo_id = tk.Entry(self)
        self.entry_nuevo_id.pack(pady=5)

        self.btn_confirmar_crear_usuario = tk.Button(self, text="Crear Usuario", command=self.crear_usuario)
        self.btn_confirmar_crear_usuario.pack(pady=5)


class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Ocultar la ventana principal al inicio
        LoginWindow(self)
        self.logo = util_img.leer_imagen("./imagenes/icono.png", (460, 336))
        self.perfil = util_img.leer_imagen("./imagenes/user.png", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()

        self.prestamos = []
        self.usuarios = []
        self.libros = []
        self.grupos = []

        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()
        self.curso = Curso()
        # Lista de usuarios predefinidos

        usuarios = [
            Usuario("Pedro", "Gomez", "001"),
            Usuario("Ana", "Martinez", "002"),
            Usuario("Luis", "Rodriguez", "003"),
            Usuario("Laura", "Diaz", "004"),
            Usuario("Carlos", "Lopez", "005"),
            Usuario("Sofia", "Sanchez", "006"),
            Usuario("Diego", "Hernandez", "007"),
            Usuario("Valentina", "Perez", "008"),
            Usuario("Andres", "Gutierrez", "009"),
            Usuario("Juliana", "Gomez", "010")
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

        profesores = [
            Profesor("Juan", "Perez"),
            Profesor("Isabela", "Garcia"),
            Profesor("Maria", "Gonzalez")
        ]

        asignaturas = [
            Asignatura("Matemáticas", profesores[0]),
            Asignatura("Física", profesores[1]),
            Asignatura("Mecánica", profesores[2])
        ]

        for asignatura in asignaturas:
            self.curso.registrar_asignaturas(asignatura)

        horarios = [
            Horario("Lunes", "08:00", "10:00"),
            Horario("Martes", "10:00", "12:00")
        ]

        for horario in horarios:
            self.curso.registrar_horarios(horario)

        evaluaciones = [
            Evaluacion(usuarios[0], 3.8),
            Evaluacion(usuarios[1], 4.5)
        ]
        for evaluacion in evaluaciones:
            self.curso.registrar_evaluaciones(evaluacion)

        grupos = [
        Grupo("DR", asignaturas[1], Horario("Lunes", "08:00", "10:00"), usuarios[4]),
        Grupo("BR", asignaturas[2], Horario("Martes", "10:00", "12:00"), usuarios[2])
        ]
        for grupo in grupos:
            self.curso.registrar_grupos(grupo)


    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def registrar_usuario(self, usuario):
        self.cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", 
                            (usuario.get_id_user(), usuario.get_nombre(), usuario.get_apellido()))
        self.conexion.commit()

    def show_main_window(self):
        self.deiconify()  # Mostrar la ventana principal

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Biblioteca')
        self.iconbitmap("./imagenes/unip.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Menú")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="black")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="correo@unipamplona.edu.co")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        
        self.buttonasignatura= tk.Button(self.menu_lateral)        
        self.buttonhorarios = tk.Button(self.menu_lateral)        
        self.buttoneva = tk.Button(self.menu_lateral)
        self.buttoncursos = tk.Button(self.menu_lateral)        
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Asignaturas", "📚", self.buttonasignatura,self.mostrar_asignaturas),
            ("Ver horario", "🕒", self.buttonhorarios,self.mostrar_horario),
            ("Evaluaciones", "📝", self.buttoneva,self.mostrar_evas),
            ("Entrar a un curso", "🚪", self.buttoncursos,self.entrar_curso),
            ("Salir", "📤", self.buttonSettings,self.destroy)
        ]
        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)                    
          

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        logo_image = Image.open("./imagenes/unip.png")
        logo_image = logo_image.resize((360, 336), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="black", width=ancho_menu, height=alto_menu,
                      command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA)

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_asignaturas(self):
        self.limpiar_cuerpo()
        cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=250, height=200)
        cuadro_texto.pack(padx=30, pady=30)

        for asignatura in self.curso.asignaturas:
            info_asignatura = f"Nombre: {asignatura.get_nombre()}\nProfesor: {asignatura.get_profesor().get_nombre()} {asignatura.get_profesor().get_apellido()}\n\n"
            cuadro_texto.insert(tk.END, info_asignatura)
        
        cuadro_texto.config(state=tk.DISABLED)


    def mostrar_horario(self):
        self.limpiar_cuerpo()
        cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=150, height=150)
        cuadro_texto.pack(padx=30, pady=30)

        for horario in self.curso.horarios:
            info_horario = f"Día: {horario.get_dia()}\nHora: {horario.get_hora_inicio()}{horario.get_hora_fin()} \n\n" 
            cuadro_texto.insert(tk.END, info_horario)                    
        
        cuadro_texto.config(state=tk.DISABLED)          


    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_evas(self):
        self.limpiar_cuerpo()
        cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=150, height=150)
        cuadro_texto.pack(padx=30, pady=30)

        for evaluacion in self.curso.evaluaciones:
            info_eva = f"Nombre del estudiante: {evaluacion.get_usuario().get_nombre()}\nApellido del Estudiante: {evaluacion.get_usuario().get_apellido()}\nNota: {evaluacion.get_nota()} \n\n" 
            cuadro_texto.insert(tk.END, info_eva)            
        
        cuadro_texto.config(state=tk.DISABLED)

    def entrar_curso(self):
        self.limpiar_cuerpo()
        def entrar():
            id_usuario = self.entry_usuario_id.get()
            nombre = self.entry_nombre_grupo.get()

            grupo = self.curso.buscar_grupo_por_nombre(nombre)
            if not grupo:
                messagebox.showerror("Error", "Curso no encontrado")
                return
            

            self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id_usuario,))
            usuario = self.cursor.fetchone()
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado")
                return

            messagebox.showinfo("Éxito", f"Te has unido al curso {nombre} con éxito")
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Ingrese su ID y el grupo del curso a ingresar:", font=("Helvetica", 16), bg=COLOR_CUERPO_PRINCIPAL)
        label_titulo.pack(pady=10)

        # Campos de entrada

        self.label_usuario_id = tk.Label(self.cuerpo_principal, text="ID Estudiante:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_usuario_id.pack(pady=5)
        self.entry_usuario_id = tk.Entry(self.cuerpo_principal)
        self.entry_usuario_id.pack(pady=5)

        self.label_nombre_grupo = tk.Label(self.cuerpo_principal, text="Curso:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_nombre_grupo.pack(pady=5)
        self.entry_nombre_grupo = tk.Entry(self.cuerpo_principal)
        self.entry_nombre_grupo.pack(pady=5)


        # Botón para confirmar el préstamo
        self.btn_confirmar_curso = tk.Button(self.cuerpo_principal, text="Unirme al curso", command=entrar)
        self.btn_confirmar_curso.pack(pady=10)    
       