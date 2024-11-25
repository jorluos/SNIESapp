class gestor_metricas:
    def __init__(self, archivo) -> None:
        self.archivo = archivo
    
    def obtener_metricas(self, filtro):
        try:
            if self.archivo[filtro].dtype == "object":
                conteo = self.archivo[filtro].value_counts()
                return conteo
            else:
                total = self.archivo[filtro].sum()
                return total
        except KeyError as e:
            raise ValueError(f"Error al obtener la suma de la columna {filtro}: {e}")
        except Exception as e:
            raise ValueError(f"Error al obtener la suma de la columna {filtro}: {e}")
        
    def consolidado(self):
        columnas_unicas = ["CÓDIGO DE LA INSTITUCIÓN", "IES_PADRE", "ID SECTOR IES",
                           "ID CARACTER", "CÓDIGO DEL DEPARTAMENTO (IES)", "CÓDIGO DEL MUNICIPIO IES",
                           "CÓDIGO SNIES DEL PROGRAMA", "ID NIVEL ACADÉMICO", "ID NIVEL DE FORMACIÓN",
                           "ID METODOLOGÍA", "ID ÁREA", "ID NÚCLEO", "ID CINE CAMPO AMPLIO", "ID CINE CAMPO ESPECIFICO",
                           "ID CINE CODIGO DETALLADO", "CÓDIGO DEL DEPARTAMENTO (PROGRAMA)", "CÓDIGO DEL MUNICIPIO (PROGRAMA)",
                           "ID SEXO", "AÑO", "SEMESTRE"]
        df_consolidado = self.archivo.groupby(columnas_unicas).sum().reset_index()
        return df_consolidado

    def agrupamiento(self, columna1, columna2):
        agrupado = self.archivo.groupby(columna1)[columna2].sum().reset_index()
        return agrupado

        

