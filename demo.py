from modules.loader import Loader

loader = Loader()

loader.load("data/2026.xlsx")    #NotImplementedError: Siguiente paso: validar columnas
#loader.load("data/pepe.xlsx")    #InvalidFileError
#loader.load("data(carpeta)")      #InvalidFileError
#loader.load("data/2026.csv")     #InvalidFormatError