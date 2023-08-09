class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
<<<<<<< HEAD
                print(f"[ ] {tarea.obtenerNombre()}" )
=======

            else:
                print("forzaremos un conflicto xd")

>>>>>>> c71e6b707de5f22170049d36e9530420b32685ff
