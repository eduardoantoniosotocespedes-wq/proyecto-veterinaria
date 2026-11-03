#base de datos, aqui se deben de crear todos los datos que se van a agregar a futuro, investiguen chicas
database = {
    "usuarios": [
        {"user_name":"superadmin","password":"admin123","rol":"superadmin"},
        {"user_name":"admin1","password":"12345","rol":"admin"},
        {"user_name": "eduardo","apellido":"soto","telefono":"64946952","direccion":"villazon","password":"eduardo123","rol":"cliente"}],
    "mascotas": [],
    "citas": [],
    "historial": []}

# Variable para saber quien está logueado
usuario_actual = None