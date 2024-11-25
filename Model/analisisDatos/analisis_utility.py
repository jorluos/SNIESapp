import streamlit as st
import pandas as pd
import os

def charge_file(uploadedfile):
    if not os.path.exists('temp'):
        os.makedirs('temp')

    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success(f'Archivo {uploadedfile.name} guardado temporalmente')

def show_files():
    directorio = 'docs/inputs'
    archivosDisponibles = os.listdir(directorio)
    st.markdown("""<div style="background-color:#494BA8; padding: 20px; border-radius: 5px;">
                                <h1>Análisis de Datos</h1>
                                <h3>Usa nuestro servicio de procesamiento de Datos </h3>
                                <img src="https://interlat.co/wp-content/uploads/2020/05/59915-2048x1363.jpg" width="300" height="auto" style="float: center; margin-left: 20px; border-radius: 5px;">
                                <img src="https://th.bing.com/th/id/OIP.1QYfWhB3mFjAxHTtL31rsgHaD5?rs=1&pid=ImgDetMain" width="auto" height="200" style="float: center; margin-left: 20px; border-radius: 5px;">
                        </div>""", unsafe_allow_html=True)
    with st.expander('Ver el listado de Archivos Disponibles en el directorio inputs'):
        if archivosDisponibles:
            for archivo in archivosDisponibles:
                st.write(archivo)
        else:
            st.write('No hay archivos disponibles en el directorio indicado')

def charge_new_file():
    # Cargar nuevos archivos
    uploadedFiles = st.file_uploader("Cargar nuevo Archivo", type=['csv', "xlsx", "txt"], accept_multiple_files=True)

    if uploadedFiles:
        for uploadedFile in uploadedFiles:
            charge_file(uploadedFile)

    subidos_button = st.button("Listo")
    if subidos_button and uploadedFiles:
        st.subheader('Archivos Subidos')
        for file in uploadedFiles:
            st.write(file.name)

            # Leer y mostrar el contenido del archivo dependiendo del tipo
            if file.type == "text/csv":
                df = pd.read_csv(file)
                st.dataframe(df)
            elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(file)
                st.dataframe(df)
            elif file.type == "text/plain":
                st.text(file.getvalue().decode("utf-8"))
    elif subidos_button:
        st.write('No has subido ningún archivo')