from API.API import *
from UI.UI import *

def main():
    filtrosUsados = obtencionDeFiltros()
    generarEstructuraDeDatos(filtrosUsados)

if __name__ == "__main__":
    main()