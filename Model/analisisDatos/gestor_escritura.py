class gestor_escritura:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar_excel(self, nombre_archivo):
        try:
            self.archivo.to_excel(nombre_archivo, index=False, engine="openpyxl")
        except Exception as e:
            raise ValueError(f"Error al guardar el archivo Excel: {e}")
    
    def guardar_json(self, nombre_archivo):
        try:
            self.archivo.to_json(nombre_archivo, index=False)
        except Exception as e:
            raise ValueError(f"Error al guardar el archivo JSON: {e}")

    def guardar_csv(self, nombre_archivo):
        try:
            self.archivo.to_csv(nombre_archivo, index=False)
        except Exception as e:
            raise ValueError(f"Error al guardar el archivo CSV: {e}")