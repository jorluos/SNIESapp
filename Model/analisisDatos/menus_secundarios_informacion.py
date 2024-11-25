import streamlit as st
import pandas as pd
import Model.analisisDatos.menu_filtros as mf
from Model.analisisDatos.gestor_lectura import gestor_lectura as gl

@st.cache_data
def cargar_datos(archivos): # Para evitar cargar datos inecesariamente
    lector = gl()
    df_principal = pd.read_excel(archivos[0], engine="openpyxl")
    lector.archivo = df_principal
    indice = lector.obtener_indice_encabezados()
    encabezados = lector.obtener_encabezados(indice)
    lector.archivo.drop(index=range(0, indice + 1), inplace=True)
    dataframes = [lector.archivo]
    for archivo in archivos[1:]:
        df = pd.read_excel(archivo, engine="openpyxl")
        df.drop(index=range(0, indice + 1), inplace=True)
        dataframes.append(df)
    datos_combinados = pd.concat(dataframes, ignore_index=True)
    datos_combinados.columns = encabezados
    
    #  Arreglar tipo de datos de la columna
    datos_combinados = corregir_tipo(datos_combinados)

    return datos_combinados

def corregir_tipo(archivo):
    for columna in archivo.columns:
        try:
            archivo[columna] = archivo[columna].astype(int)
        except ValueError:
            pass
    return archivo

def obtener_valores_sin_repeticion(columna, archivo):
    if columna in archivo.columns:
        valores_unicos = archivo[columna].unique().tolist()
        return valores_unicos
    else:
        raise ValueError(f"La columna {columna} no existe")

def boton_volver():
    if st.button("Volver", key="volver"):
        st.session_state["menu"] = "primero"

def boton_descargar():
    if st.button("Descargar informacion"):
        st.session_state["menu"] = "descargar"

def boton_estadisticas():
    if st.button("Analizar estadisticas"):
        st.session_state["menu"] = "estadisticas"

def boton_ver_informacion():
    if st.button("Ver Informacion"):
        st.session_state["menu"] = "Ver Informacion"

def menu_seleccion_filtro():
    col1, col2 = st.columns(2)
    with col1:
        st.title(f"Menu de :violet[{st.session_state['categoria']}]")
        boton_volver()
        try:
            lector = gl()
            base_path = "docs/inputs"
            archivos = lector.obtener_archivos_rango(st.session_state["rango"], st.session_state["categoria"], base_path)
            datos = cargar_datos(archivos)
            lector.archivo = datos
            encabezados = lector.archivo.columns
            filtro_columna = st.selectbox(
                "Selecciona uno de los filtros",
                options=encabezados
            )
            st.session_state["filtro_columna"] = filtro_columna
            st.session_state["dataframe"] = lector.archivo
            if filtro_columna:
                opciones_filtros(lector, filtro_columna)
        except Exception as e:
            st.error(f"Error al seleccionar el filtro: {e}")
        boton_ver_informacion()
        boton_descargar()
        boton_estadisticas()
    with col2:
        st.markdown(
            """<img src="https://www.pinclipart.com/picdir/big/529-5296542_analysis-data-clipart.png" width="auto" height="auto">""",
            unsafe_allow_html=True)


def opciones_filtros(lector, filtro):
    columna_seleccionada = lector.obtener_columna(filtro).iloc[:, 0]
    if lector.columna_numerica(columna_seleccionada):
        st.session_state["fila_filtro"] = mf.opcion_entrada_texto()
    elif lector.columna_string(columna_seleccionada):
        opciones = obtener_valores_sin_repeticion(filtro, lector.archivo)
        st.session_state["fila_filtro"] = mf.opcion_caja_seleccion(opciones)

