def volver_menu(cuenta, ventana):
    from src.ui_main.Menu_inicial import Menu_inicial
    if "Administrativo" in cuenta.rol:
        Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
    else:
        Menu_inicial.menu_inicial_Clinico(cuenta, ventana)
