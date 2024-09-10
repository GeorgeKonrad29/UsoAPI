def obtencionDeFiltros():
    entradasUsuario = ""
    listaDeFiltros = {}
    while entradasUsuario != "f":
        entradasUsuario = str(input("Por favor escriba que desea agregar al filtro o solo la inicial:\n"
                                    "departamento\n"
                                    "municipio\n"
                                    "cultivo\n"
                                    "Si desea finalizar escribir: \"f\"\n"))
        listaDeFiltros = escribirEnListaFiltros(entradasUsuario, listaDeFiltros)
    listaDeFiltros['limit']= recibirCantidadDeDatosDeseados()
    print("Generando informe...\n")
    return listaDeFiltros


def escribirEnListaFiltros(entradasUsuario, listaDeFiltros):
    if entradasUsuario in "departamento":
        departamentoIngresado = str(input("Por favor escriba el departamento:\n"))
        departamentoIngresado = departamentoIngresado.upper()
        listaDeFiltros['departamento'] = departamentoIngresado
    elif entradasUsuario in "municipio":
        municipioIngresado = str(input("Por favor escriba el municipio:\n"))
        municipioIngresado = municipioIngresado.upper()
        listaDeFiltros['municipio'] = municipioIngresado
    elif entradasUsuario in "cultivo":
        cultivoIngresado = str(input("Por favor escriba el cultivo:\n"))
        cultivoIngresado = cultivoIngresado.upper()
        listaDeFiltros['cultivo'] = cultivoIngresado
    elif entradasUsuario == "f":
        print("\n")
    else:
        print("Filtro no válido")

    return listaDeFiltros
def recibirCantidadDeDatosDeseados():
    cantidadDeDatos = 0
    while cantidadDeDatos <= 0:
        cantidadDeDatos = int(input("Ingrese la cantidad de datos que desea recibir:\n"))
        if cantidadDeDatos < 0 or cantidadDeDatos == 0:
            print("cantidad de datos no valida")

    return cantidadDeDatos