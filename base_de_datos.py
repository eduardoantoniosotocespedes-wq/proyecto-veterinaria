#base de datos, aqui se deben de crear todos los datos que se van a agregar a futuro, investiguen chicas
database = {
    "usuarios": []}

#parte del codigo que crea al owner por defecto en la base de datos, el administrador que siempre va a existir
if len(database["usuarios"])== 0:
    database["usuarios"].append({
        "user_name":"superadmin",
        "password":"admin123",
        "rol":"superadmin"})