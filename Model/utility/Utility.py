import streamlit as st
import os

def html_code():
    html_code = """
    <!DOCTYPE html> 
    <html lang="es"> 
    <head> 
        <meta charset="UTF-8"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <title>SNIES</title> 
        <style> 
            body { 
                font-family: Arial, sans-serif; 
                } .header { 
                text-align: center; 
                padding: 40px; 
                background-color: #5153AC; 
                color: white;
                } .banner{ 
                display: flex; 
                justify-content: flex-start; 
                background-color: #5153AC; 
                color: white;
                padding: 10px; 
                align-items: flex-start;
                } .banner img{ 
                    max-width: 55%; 
                    height: auto; 
                } .container {
                     position: relative; 
                     max-width: 100%; 
                }.zoom {
                    transition: transform 0.5s ease;
                } .container:hover .zoom {
                    transform: scale(1.1);
                }.content { 
                    display: flex; 
                    justify-content: space-around; 
                    padding: 20px; 
                    background-color: #494BA8;
                    color: white;
                } .left, .right { 
                    width: 45%; 
                } .right button { 
                    width: 100%; 
                    padding: 10px; 
                    background-color: #FFFFFF;
                    color: #494BA8;
                    padding: 15px 32px;
                    text-align: center;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 4px;
                } .button {
                    background-color: #FFFFFF;
                    border: none;
                    color: #494BA8;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 4px;
                }

        </style> 
    </head> 
    <body> 
        <div class="header"> 
            <h1>Sistema Nacional de Información de la Educación Superior (SNIES)</h1> 
        </div> 
        <div class="banner"> 
            <img src="https://www.cna.gov.co/1779/articles-402145_logo.png"  class="zoom" </img><p> 
            <div class="banner"> 
                <div>
                    <p style="font-size: 25px;">Conozca las instituciones y programas académicos de educación superior autorizados por el Ministerio de Educación Nacional</p>
                    <div class="right">
                        <a href="https://snies.mineducacion.gov.co/portal/" class="button">SNIES portal</a>
                        <a href="https://www.ebc.mx/que-es-un-programa-academico/#:~:text=B%C3%A1sicamente%20es%20un%20plan%20de%20estudios%20detallado%2C%20donde,notar%C3%A1s%20que%20poseen%20un%20modelo%20de%20programa%20acad%C3%A9mico." class="button">Programas</button></a>
                    </div>
                </div>
            </div> 
        </div> 
        <div class="content"> 
            <div class="left"> 
                <h2>Educación</h2> 
                <p style="font-size: 20px;">Sabías que en Colombia, las instituciones de educación superior (IES) se clasifican en tres categorías principales:<br>
                 Instituciones Técnicas Profesionales, Instituciones Tecnológicas y Universidades.<br>
                Cada una ofrece programas de pregrado y posgrado en diversas áreas.</p> 
                <p style="font-size: 20px;">Este sistema provee información detallada sobre las instituciones y programas de educación superior en Colombia.</p> 
                <div class="container">
                    <img src="https://static.misionesonline.news/wp-content/uploads/2020/11/Clases-universitarias-AP-def.jpg" class="zoom"</img>
                </div>
            </div> 
            <div class="container"> 
                 <img src="https://www.pngarts.com/files/7/Education-Course-Download-Transparent-PNG-Image.png" width="800" height="700"  class="zoom"</img>
            </div>
        </div> 
    </body> 
    </html>
    """
    return html_code

def html_code2():
    html_code = """<div style="background-color:#494BA8; padding: 20px; border-radius: 5px;">
                            <p style="font-size: 20px;">El Sistema Nacional de Información de la Educación Superior (SNIES) en Colombia recopila datos detallados sobre las 
                            instituciones y programas académicos de educación superior. Este análisis de datos, que abarca aspectos como inscripción, 
                            admisión, matrícula y graduación, es fundamental para tomar decisiones informadas en el ámbito educativo.
                            </p>
                    </div>
                    <div>
                        <img src="https://www.uniautonoma.edu.co/sites/default/files/evento/g.jpg">
                    </div>"""
    return html_code

def html_code3():
    html_code = """ <div style="background-color:#494BA8; padding: 20px; border-radius: 5px;">
                            <h3>Mejora del Diseño Curricular</h3><p style="font-size: 20px;">El análisis de las tendencias de 
                                matrícula y graduación puede identificar áreas que necesitan ajustes curriculares, asegurando 
                                que los programas sean relevantes y atractivos para los estudiantes.</p>
                            <h3>Decisiones Estratégicas</h3><p style="font-size: 20px;">Datos históricos y tendencias ayudan a las 
                            instituciones a decidir sobre la apertura de nuevos programas, modificaciones de los existentes, y la 
                            asignación de recursos. Esto permite a las instituciones responder de manera proactiva a las demandas 
                            del mercado educativo y laboral.</p>
                    </div>"""
    return html_code


def save_coments(comentarios, persona, coment):
    comentarios.append({"persona": persona, "comentario": coment})

def coments(comentarios):
    st.markdown("<p style='font-size: 30px;'>Ayudanos a Mejorar!!!<br>Dejanos conocer tu opinión</p>", unsafe_allow_html=True)
    comentario = st.text_input("Escribe tus comentarios")
    persona = st.text_input('Escribe tu Nombre por favor')
    comentario_button = st.button('Enviar Comentarios')
    if comentario and persona and comentario_button:
        st.write('Tus comentarios han sido enviados con éxito')
        save_coments(comentarios, persona, comentario)
    elif comentario_button:
        st.write('No has escrito ningún comentario')







