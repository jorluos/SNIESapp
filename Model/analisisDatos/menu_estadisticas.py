import plotly.express as px
import streamlit as st
from Model.analisisDatos.gestor_metricas import gestor_metricas as gm
from Model.analisisDatos.gestor_lectura import gestor_lectura as gl

def boton_volver_categoria():
    if st.button("Volver", key="volver"):
        st.session_state["menu"] = st.session_state["categoria"]

def obtener_grafico():
    boton_volver_categoria()
    categoria = st.session_state["categoria"]
    rango = st.session_state["rango"]
    st.title(f"Datos estadisticos de {categoria} años {rango}")
    lectura = gl(st.session_state["dataframe"])
    consolidado = gm(lectura.archivo)
    tabla = consolidado.agrupamiento("INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)",
                                     str.upper(categoria))
    tabla2 = consolidado.agrupamiento("SEXO", str.upper(categoria))

    tabla3 = consolidado.agrupamiento("AÑO", str.upper(categoria))
    
    tabla4 = consolidado.agrupamiento("DEPARTAMENTO DE DOMICILIO DE LA IES", str.upper(categoria))

    tabla5 = consolidado.agrupamiento("DESC CINE CAMPO ESPECIFICO", str.upper(categoria))

    tabla6 = consolidado.agrupamiento("SEMESTRE", str.upper(categoria))

    generar_grafico_barras(tabla, categoria, "INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)")
    generar_grafico_barras(tabla2, categoria, "SEXO")
    generar_grafico_barras(tabla3, categoria, "AÑO")
    generar_grafico_barras(tabla4, categoria, "DEPARTAMENTO DE DOMICILIO DE LA IES")
    generar_grafico_barras(tabla5, categoria, "DESC CINE CAMPO ESPECIFICO")
    generar_grafico_barras(tabla6, categoria, "SEMESTRE")

    


def generar_grafico_barras(archivo, categoria, columna):
    fig = px.bar(
    archivo,
    x=columna,
    y=str.upper(categoria),
    color=columna,
    title=f"{str.upper(categoria)} POR {columna}",
    labels={f"NUMERO DE {categoria}": f"Número de {categoria}"},
    width=1500,  # Ajusta el ancho del gráfico
    height=800  # Ajusta la altura del gráfico
    )
    st.plotly_chart(fig)


