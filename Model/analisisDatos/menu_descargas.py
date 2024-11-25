import streamlit as st
from Model.analisisDatos.gestor_escritura import gestor_escritura as ge
from Model.analisisDatos.gestor_lectura import gestor_lectura as gl

def menu_descargas():
    boton_volver_categoria()
    st.title("Descarga tu informacion :blue[PERSONALIZADA] 🤪")
    st.markdown("## Descargas ")
    st.markdown("### Aquí puedes descargar el archivo con la información filtrada del Sistema Nacional de Información de la Educación Superior (SNIES).")
    try:
        lector = gl(st.session_state["dataframe"])
        filtrado = lector.obtener_filas_filtro(st.session_state["filtro_columna"], st.session_state["fila_filtro"])
        descarga = ge(filtrado)
        tipo_descarga = st.selectbox(
            "Selecciona el tipo de archivo que deseas para tu descarga",
            options= ["Excel", "Json", "CSV"]
        )
        boton_descargar(tipo_descarga, descarga)
    except Exception as e:
        st.error(f"Error en la descarga {e}")
    st.markdown("### El contenido se genera según los criterios establecidos en tu consulta. Asegúrate de guardar el archivo para futuras referencias.")

def boton_volver_categoria():
    if st.button("Volver", key="volver"):
        st.session_state["menu"] = st.session_state["categoria"]

def boton_descargar(opcion, escritor):
    if st.button("Descargar"):
        if opcion == "CSV":
            escritor.guardar_csv("informacionPersonalizada.csv")
        elif opcion == "Json":
            escritor.guardar_json("informacionPersonalizada.json")
        elif opcion == "Excel":
            escritor.guardar_excel("informacionPersonalizada.xlsx")