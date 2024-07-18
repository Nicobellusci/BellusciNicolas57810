#_______________________________________________________________________________________________________

Bellusci Nicolas
Curso: Python
Comisión 57810
Proyecto Final titulado: "La Cantina di Giuseppe"

    Es un sitio WEB de un local de comidas rápidas, que permite:
        -Acceso al menu y el CRUD de los modelos si el usuario esta logueado.
        -Un Filtro de busqueda sobre el modelo de "Entradas".
        -Registrarse, iniciar sesión y cerrar sesión.
        -Editar el perfil de usuario.
        -Cambiar password.
        -Actualizar el Avatar.
    
    Carpeta raiz ProyectoResto:
    Modelos: Entradas, Pizzas, Hamburguesas y Empanadas + Avatar    

    Video Resumen:
    https://www.youtube.com/watch?v=tLyOUtaqwzA


#______USUARIOS___________________________________________________________________________________

    #_____Panel de administración:

        http://127.0.0.1:8000/admin/
            User: Admin
            Pass: Temporal123

    #_____Registro de usuarios por formulario:

        User: servernb
        Pass: Temporal789* --> cambio a --> newpass: Vacio*999 --> newpass2: Vacio*147

        User: servernb2
        Pass: Temporal789*

        User: Barco788
        pass: Temporal123

            User: mmarta999
            pass: Temporal123


#______RUTAS DE ACCESO___________________________________________________________________________________

    #_____Home:

    http://127.0.0.1:8000/        
    
    
    #_____Menu:

    http://127.0.0.1:8000/Entradas/
    http://127.0.0.1:8000/Pizzas/
    http://127.0.0.1:8000/Burgers/
    http://127.0.0.1:8000/Empanadas/
    

    #_____Formularios de ingreso de datos:

        http://127.0.0.1:8000/EntradasForm/
        http://127.0.0.1:8000/PizzasForm/
        http://127.0.0.1:8000/BurgersForm/
        http://127.0.0.1:8000/EmpanadasForm/
        

    #_____Formulario Busqueda:

        http://127.0.0.1:8000/buscarEntradas/


    #_____Acerca:
    
        http://127.0.0.1:8000/Acerca/



______TEST______________________________________________________________________________________________
    Accesos a los menus - OK
    Acceso a Acerca - OK
    Crear una entrada en los menus - OK
    CRUD en las entradas - OK
    Buscar una entrada - OK
    Login - OK
    Falso Login - OK
    Registro de usuario - OK
    Logout - OK
    Restriccion de acceso por login - OK
    Editar perfil - OK
    Cambiar clave - OK
    Actualizar Avatar - OK









