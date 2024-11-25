import streamlit as st
from Model.utility.Utility import html_code, html_code2, html_code3, coments


def iniciar_programa():
    st.set_page_config(page_title="Inicio", page_icon="😎", layout="wide", initial_sidebar_state="collapsed")  # Configuración general de la página

    # Apartado de html de la página principal
    html_code_var = html_code()
    st.markdown(html_code_var, unsafe_allow_html=True)
    st.write('')

    col1, col2, col3 = st.columns(3)
    with col1 :
        st.title('SNIES')
        html_code2_var = html_code2()
        st.markdown(html_code2_var, unsafe_allow_html=True)

        # Apartado de comentarios para mejorar
        comentarios = []
        coments(comentarios)

    with col2:
        st.title('Importancia del Análisis de Datos')
        html_code3_var = html_code3()
        st.markdown(html_code3_var, unsafe_allow_html=True)

    with col3:

        tab1, tab2 = st.tabs(["DATOS DE INTERÉS", "INFORMACIÓN"])  # Apartadi de pestañas para inmersión de la página
        with tab1:
            st.header("DATOS DE INTERÉS")
            st.write("Mantente informado con estos datos que podrían interesarte.")

            # Ejemplo de una lista de noticias
            noticias = [ {"titulo": "¿Conoces el SNIES?", "descripcion": "Aprende sobre lo que es y lo que hace el SNIES", "link": "https://www.mineducacion.gov.co/sistemasinfo/InformacionInstitucional/211868:Que-es-el-SNIES", "video": "https://www.youtube.com/watch?v=dFmZbTBSMN4"},
                         {"titulo": "¿No sabes como usar el SNIES?", "descripcion": "Descubre paso a paso como usar el SNIES de manera eficiente", "link": "https://snies.mineducacion.gov.co/portal/EL-SNIES/Como-funciona/", "video": "https://youtu.be/fPWI19h4P38"}
            ]

            for noticia in noticias:
                st.subheader(noticia["titulo"])
                st.write(noticia["descripcion"])
                st.markdown(f"[Lee más]({noticia['link']})")
                st.video(noticia["video"])

        with tab2:
            st.header('Conoce más sobre nosotros')
            st.write('Github de las personas implicadas en el desarrollo:')
            link_git = [{"integrante": "Jorge", "gitHub": "https://github.com/jorluos"},
                       {"integrante": "Alejandro", "gitHub": "https://github.com/Alejost7"},
                       {"integrante": "Mateo", "gitHub": "https://github.com/Mateo"}]

            for integrante in link_git:
                st.write(integrante["integrante"], ":")
                st.write(integrante["gitHub"])
            st.markdown('#### Agradecimientos')
            st.video('https://youtu.be/HjhXZufoIeI')
            st.subheader('Echa un vistazo al Manual Técnico de esta aplicación web')
            ruta_archivo = 'https://github.com/300CIS017-Object-Oriented-Programming/proyecto-3-pinche_trump/blob/d99d05bc03edc57dad72305e1c900d89be8dfd09/README.md'
            enlace_html = f"""<a href="{ruta_archivo}" target="_blank" style="font-size: 20px; color: #007BFF; text-decoration: none;">Ver manual Técnico</a>"""
            st.markdown(enlace_html, unsafe_allow_html=True)

if __name__ == "__main__":
    iniciar_programa()

