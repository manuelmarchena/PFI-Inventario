from datetime import datetime
import curses
#* Funciones responsables del llamado por INPUT

usuarios: list = ['manuel', 'adriana']
# TODO hay que hacer la parte de CRUD de Usuarios
name: str = ''
date: str = datetime.today()
print(date)
registro_usuarios: dict = {
    "usuario": name,
    "fecha": date,
    }


def validar_usuario(name: str):
    if name in usuarios:
        curses.wrapper(menu_opciones)
        return True
    else:
        return False

menu = ['Opción 1', 'Opción 2', 'Opción 3', 'Salir']
def menu_opciones(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    current_row = 0

    while True:
        stdscr.clear()  # Limpiar la pantalla en cada actualización

        # Mostrar las opciones del menú
        for idx, row in enumerate(menu):
            if idx == current_row:
                stdscr.addstr(idx, 0, f"> {row}", curses.A_REVERSE)  # La opción seleccionada en reverso
            else:
                stdscr.addstr(idx, 0, row)

        # Refrescar la pantalla para que los cambios se vean
        stdscr.refresh()

        # Esperar entrada de teclado
        key = stdscr.getch()

        # Navegar por las opciones con las flechas
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
            if current_row == len(menu) - 1:  # Salir si selecciona la última opción
                break
            else:
                stdscr.addstr(len(menu) + 1, 0, f"Has seleccionado '{menu[current_row]}'")
                stdscr.refresh()
                stdscr.getch()  # Pausa para que el usuario vea el mensaje

def saludar():
    print("Hola! Bienvenido a la app de control de inventario \n")
    name: str = input("Para empezar dime tu nombre de usuario, este nombre se verificará en los registros y si existe guardará como registro de que usuario realizó los cambios: ")
    if validar_usuario(name):
        print(f"Muy bien {str.capitalize(name)}, podemos empezar, que operación vas a realizar")
        return True
    else:
        return False


nombre = saludar()
validar_usuario(nombre)
