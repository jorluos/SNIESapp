import streamlit as st
import Model.analisisDatos.menus_secundarios_informacion as msi
import Model.analisisDatos.menu_descargas as md
import Model.analisisDatos.menu_ver_informacion as mvi
import Model.analisisDatos.menu_estadisticas as me
from Model.analisisDatos.analisis_utility import *

def primer_menu():
    st.set_page_config(page_title="Analizar Datos", layout="wide", page_icon="🤪", initial_sidebar_state="collapsed")
    show_files()

    tab1, tab2 = st.tabs(["CARGAR ARCHIVOS NUEVOS", "PROCESAR DATOS"])
    with tab1:
        st.subheader("Gestión de Archivos")
        st.subheader(":green[Carga Nuevos Archivos Para el Análisis]")
        st.markdown("##### Una vez que hayas cargado los archivos que quieras incluir en el análisis pasa a la pestaña de procesar Datos para continuar")
        charge_new_file()
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.title('Procesemos tus Datos')
            st.markdown("### Depués de procesar los datos aprovecha y Descarga informacion personalizada con nuestros :red[FILTROS] 🤪")
            try:
                rango = st.slider(
                    "Selecciona un rango de años",
                    min_value=2020,
                    max_value=2023,
                    value=(2020,2023)
                    )
            except Exception as e:
                st.error(f"Error al seleccionar el rango: {e}")

            try:
                categoria_archivo = st.selectbox(
                    "Que categoria desea comparar?",
                    options=["admitidos", "graduados", "inscritos", "matriculados", "matriculadosPrimeraVez"],
                )
            except Exception as e:
                st.error(f"Error al seleccionar la categoria: {e}")

            if st.button("Listo", key="listo"):
                st.session_state["rango"] = rango
                st.session_state["categoria"] = categoria_archivo
                st.session_state["menu"] = categoria_archivo
        with col2:
            st.markdown("""<img src="https://hiades.es/wp-content/uploads/2020/06/proceso1c.png" width="auto" height="auto">""", unsafe_allow_html=True)

def app():
    if "menu" not in st.session_state:
        st.session_state["menu"] = "primero"

    if st.session_state["menu"] == "primero":
        primer_menu()
    elif st.session_state["menu"] == st.session_state["categoria"]:
        msi.menu_seleccion_filtro()
    elif st.session_state["menu"] == "descargar":
        md.menu_descargas()
    elif st.session_state["menu"] == "Ver Informacion":
        mvi.menu_ver_informacion()
    elif st.session_state["menu"] == "estadisticas":
        me.obtener_grafico()
    else:
        st.write('opcion de menu no reconocida')

app()