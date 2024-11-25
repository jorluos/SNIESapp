import pandas as pd
import streamlit as st
import os

class gestor_lectura:
    def __init__(self, archivo=None):
        if archivo is not None:
            self.archivo = archivo
        else:
            self.archivo = pd.DataFrame()

    def obtener_indice_encabezados(self):
        index = self.archivo[self.archivo.iloc[:, 0] == "CÓDIGO DE LA INSTITUCIÓN"].index
        if not index.empty:
            return index[0]
        else:
            return None

    def obtener_encabezados(self, index):
        header = self.archivo.iloc[index]
        return header.values.flatten().tolist()  #  retornar una lista plana (retornaba una lista 3D)

    def obtener_filas_filtro(self, columna_filtro, fila_filtro):
        filas_con_filtro = self.archivo[self.archivo[columna_filtro] == fila_filtro]
        if not filas_con_filtro.empty:
            return filas_con_filtro
        else:
            raise ValueError(f"No se encontraron filas con el filtro: {fila_filtro}")
        
    def obtener_archivos_rango(self, rango, categoria, base_path):
        i = rango[0]
        lista_archivos = []
        while i <= rango[1]:
            aux_rangos = os.path.join(base_path, f"{categoria}{i}.xlsx")
            lista_archivos.append(aux_rangos)
            i += 1
        st.markdown(lista_archivos)
        return lista_archivos
    
    def columna_numerica(self, filtro_columna):
        return pd.api.types.is_numeric_dtype(filtro_columna)
    
    def columna_string(self, filtro_columna):
        return filtro_columna.dtype == "object"
    
    def obtener_columna(self, filtro_columna):
        if filtro_columna in self.archivo.columns:
            return self.archivo[[filtro_columna]]
        else:
            raise ValueError(f"La columna {filtro_columna} no existe")