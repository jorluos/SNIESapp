import streamlit as st

def opcion_caja_seleccion(filtro):
    try:
        opcion_seleccionada = st.selectbox(
            "Por favor seleccione alguna de las opciones",
            options=filtro
        )
    except Exception as e:
        st.error(f"Error al ingresar la opcion: {e}")
    return opcion_seleccionada

def opcion_entrada_texto():
    try:
        entrada_ingresada = st.text_input("Por favor ingrese un codigo valido")
    except Exception as e:
        st.error(f"Error al ingresar la opcion: {e}")
    return entrada_ingresada